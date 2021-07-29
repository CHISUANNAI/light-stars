from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from BBS import comment, views



urlpatterns = [
   # path('list_BBS_content/',views.dispatcher)
   path('list_BBS_content',views.dispatcher),
   path('comment',comment.dispatcher),
   path("open_post",views.open_post,name='open_post')
]
