# Generated by Django 3.2.5 on 2021-07-26 07:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sick_children',
            fields=[
                ('患病儿童姓名', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='姓名')),
                ('身份证号', models.CharField(max_length=18, null=True, verbose_name='身份证号')),
                ('是否实名认证', models.BooleanField(default=0, verbose_name='是否实名认证')),
                ('年龄', models.IntegerField(default=0, verbose_name='年龄')),
                ('性别', models.CharField(max_length=4, null=True, verbose_name='性别')),
                ('是否通过患病认证', models.BooleanField(default=0, verbose_name='是否通过患病认证')),
            ],
            options={
                'db_table': '患病儿童',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('用户ID', models.CharField(max_length=8, primary_key=True, serialize=False, verbose_name='用户ID')),
                ('用户类型', models.CharField(max_length=8, null=True, verbose_name='用户类型')),
                ('姓名_组织名', models.CharField(max_length=20, null=True, verbose_name='姓名')),
                ('密码', models.CharField(max_length=128, null=True, verbose_name='密码')),
                ('身份证号', models.CharField(max_length=18, null=True, verbose_name='身份证号')),
                ('邮箱', models.EmailField(max_length=128, null=True, verbose_name='邮箱')),
                ('手机号', models.CharField(max_length=11, null=True, verbose_name='手机号')),
                ('是否实名认证', models.BooleanField(default=0, null=True, verbose_name='是否实名认证')),
                ('家庭年收入', models.CharField(max_length=20, null=True, verbose_name='家庭年收入')),
                ('是否通过家庭收入认证', models.BooleanField(default=0, null=True, verbose_name='是否通过家庭收入认证')),
                ('居住城市', models.CharField(max_length=20, null=True, verbose_name='居住城市')),
                ('是否通过社会组织认证', models.BooleanField(default=0, null=True, verbose_name='是否通过社会组织认证')),
                ('组织类型', models.CharField(max_length=5, null=True, verbose_name='组织类型')),
                ('组织描述', models.CharField(max_length=200, null=True, verbose_name='组织描述')),
            ],
            options={
                'db_table': '普通用户',
            },
        ),
        migrations.CreateModel(
            name='parent_children',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('患病儿童', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='user_data.sick_children')),
                ('用户', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='user_data.user')),
            ],
            options={
                'db_table': '监护人_患儿',
                'unique_together': {('用户', '患病儿童')},
            },
        ),
    ]
