from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    # 文章分类
    name = models.CharField(max_length=100)


class Tag(models.Model):
    # 文章标签
    name = models.CharField(max_length=70)


class Post(models.Model):
    # 文章标题
    title = models.CharField(max_length=70)
    # 文章正文
    body = models.TextField()
    # 创作时间
    create_time = models.DateTimeField()
    # 修改时间
    modified_time = models.DateTimeField()
    # 文章摘要
    excerpt = models.CharField(max_length=200,blank=True)
    # 分类与文章的关系是一对多，在多方设置外键
    category = models.ForeignKey(Category)
    # 标签与文章的关系是多对多的关系
    tags = models.ManyToManyField(Tag,blank=True)
    author = models.ForeignKey(User)

