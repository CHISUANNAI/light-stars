from django.db import models


# 用户(用户ID,用户类型,密码,邮箱,手机号,是否实名认证,姓名,身份证号,家庭年收入,
# 是否通过家庭收入认证,居住城市, 是否通过社会组织认证,组织类型,组织描述)
# 鉴护人-患儿(用户ID[f],患病儿童姓名[f])

class User(models.Model):
    用户ID = models.CharField('用户ID', max_length=8,primary_key=True)
    用户类型 = models.CharField('用户类型', null=True, max_length=8)
    姓名_组织名 = models.CharField('姓名', null=True, max_length=20)
    密码 = models.CharField('密码', null=True, max_length=128)
    身份证号 = models.CharField('身份证号', null=True, max_length=18)
    邮箱 = models.EmailField('邮箱', null=True, max_length=128)
    手机号 = models.CharField('手机号', null=True, max_length=11)
    是否实名认证 = models.BooleanField('是否实名认证', null=True, default=0)
    家庭年收入 = models.CharField('家庭年收入', null=True, max_length=20)
    是否通过家庭收入认证 = models.BooleanField('是否通过家庭收入认证', null=True, default=0)
    居住城市 = models.CharField('居住城市', null=True, max_length=20)
    是否通过社会组织认证 = models.BooleanField('是否通过社会组织认证', null=True, default=0)
    组织类型 = models.CharField('组织类型', null=True, max_length=5)
    组织描述 = models.CharField('组织描述', null=True, max_length=200)

    class Meta:
        db_table = '普通用户'


class Sick_children(models.Model):
    患病儿童姓名 = models.CharField('姓名', max_length=20, primary_key=True)
    身份证号 = models.CharField('身份证号', null=True, max_length=18)
    是否实名认证 = models.BooleanField('是否实名认证', null=False, default=0)
    年龄 = models.IntegerField('年龄', null=False, default=0)
    性别 = models.CharField('性别', null=True, max_length=4)
    是否通过患病认证 = models.BooleanField('是否通过患病认证', null=False, default=0)

    class Meta:
        db_table = '患病儿童'


class parent_children(models.Model):
    用户 = models.ForeignKey(User, on_delete=models.PROTECT)
    患病儿童 = models.ForeignKey(Sick_children, on_delete=models.PROTECT)

    class Meta:
        db_table = '监护人_患儿'
        unique_together = (("用户", "患病儿童"),)

# !患病儿童(患病儿童姓名,是否实名认证,身份证号,是否通过患病认证,年龄,性别)
