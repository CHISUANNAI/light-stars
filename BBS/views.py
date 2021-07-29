# import typing_extensions
from os import umask
from django.db.models.fields import CommaSeparatedIntegerField
from django.shortcuts import render
import json
from django.http import JsonResponse
from BBS.BBS_models import Bbsdata, Comment_data
from user_data.user_data_models import User
from user_apply_data.models import User_thumb_post,User_collect_post
# Create your views here.
from django.http import HttpResponse
import datetime

def open_post(request):
    posttitle=request.GET.get('posttitle')
    return render(request,'post-content.html',{"posttitle":json.dumps(posttitle)})

def dispatcher(request):
    # 将请求参数统一放入request 的 params 属性中，方便后续处理

    # GET请求 参数在url中，同过request 对象的 GET属性获取
    if request.method == 'GET':
        request.params = request.GET

    # POST/PUT/DELETE 请求 参数 从 request 对象的 body 属性中获取
    elif request.method in ['POST', 'PUT', 'DELETE']:
        # 根据接口，POST/PUT/DELETE 请求的消息体都是 json格式
        request.params = json.loads(request.body)

    # 根据不同的action分派给不同的函数进行处理
    action = request.params['action']
    if action == 'list_partial_title':
        return list_partial_title(request)

    elif action == 'list_one_content':
        return list_one_content(request)
       
    elif action == 'add_thumb':
        return add_thumb(request)
   
    elif action == 'add_collection':
        return add_collection(request)
    
    elif action == 'add_post':
        return add_post(request)
'''
    else:
        return JsonResponse({'ret': 1, 'msg': '不支持该类型http请求'})
'''

#发出标题信息，列出标题对应的帖子全部信息、楼层评论
def list_one_content(request):
 
    
    title = request.params['title']
    try:
        # 根据 title 找到相应的帖子记录
        post= Bbsdata.objects.get(帖子标题=title)
    except Bbsdata.DoesNotExist:
        return  {
                'ret': 1,
                'msg': '帖子被删除！'
        }
    post.浏览次数+=1
    post.save()
    #找到帖子有关信息
    qs= Bbsdata.objects.values()
    qs = qs.filter(帖子标题=title)
    postcontent = list(qs)
    s=postcontent[0]["用户_id"]
    s1 =User.objects.get(用户ID=s)
    postcontent[0]["用户_id"]=s1.姓名_组织名
    #找到帖子的评论有关信息
    cn = Bbsdata.objects.get(帖子标题=title)
    commentlist=Comment_data.objects.filter(帖子标题_id=cn).values()
    commentlist=list(commentlist)
    i=len(commentlist)
    for j in range(i):
        k=commentlist[j]["用户_id"]
        s1 = User.objects.get(用户ID=k)
        commentlist[j]["用户_id"]=s1.姓名_组织名

   # s1 = Comment_data.objects.filter(帖子标题_id=cn)

    return JsonResponse({'ret': 0, 'postcontent': postcontent,'commentlist': commentlist})

 # 发出论坛分区，列出论坛数据并按浏览量排序
def list_partial_title(request):
   
    qs = Bbsdata.objects.values()
    catalog = request.params['catalog']
    qs = qs.filter(论坛分区=catalog).order_by("-浏览次数")
    
    # 将 QuerySet 对象 转化为 list 类型
    # 否则不能 被 转化为 JSON 字符串'''
    retlist = list(qs)
    j=len(list(qs))
    return JsonResponse({'ret': 0, 'retlist': retlist,"count":j})


def add_thumb(request):

     title = request.params['title']
     userID = request.params['userID']
     try:
        record = User_thumb_post.objects.create(点赞时间=datetime.datetime.now(),帖子_id=title,用户_id=userID)
     except:
        return  JsonResponse({
                'ret': 1,
                'msg': "您已经点过赞了！"
        })
     try:
        # 根据 title 找到相应的帖子记录
        post= Bbsdata.objects.get(帖子标题=title)
     except Bbsdata.DoesNotExist:
        return  {
                'ret': 1,
                'msg': '帖子被删除！'
        }
     post.点赞数+=1
     post.save()
     return JsonResponse({'ret': 0, '点赞时间':record.点赞时间})

def add_collection(request):
    
     title = request.params['title']
     userID = request.params['userID']
     try:
        record = User_collect_post.objects.create(收藏时间=datetime.datetime.now(),帖子_id=title,用户_id=userID)
     except:
        return  JsonResponse({
                'ret': 1,
                'msg': "您已经收藏过了！"
        })
     try:
        # 根据 title 找到相应的帖子记录
        post= Bbsdata.objects.get(帖子标题=title)
     except Bbsdata.DoesNotExist:
        return  {
                'ret': 1,
                'msg': '帖子被删除！'
        }
     post.收藏数+=1
     post.save()
     return JsonResponse({'ret': 0, '收藏时间':record.收藏时间})

def add_post(request):
    
     title = request.params['title']
     postcontent = request.params['postcontent']
     userid = request.params['userid']
     catalog = request.params['catalog']
     try:
        record = Bbsdata.objects.create(帖子标题=title,帖子内容=postcontent,发帖时间=datetime.datetime.now(),论坛分区=catalog,点赞数=0,收藏数=0,浏览次数=0,是否审核通过=0,用户_id=userid)
     except:
        return  JsonResponse({
                'ret': 1,
                'msg': "发帖失败！请更换标题避免重复。"
        })
     record.save()
     return JsonResponse({'ret': 0})

     
     

