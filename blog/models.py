from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import redirect
from django.urls import reverse


class Category(models.Model):
    # 文章分类
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    # 文章标签
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name


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
    excerpt = models.CharField(max_length=200, blank=True)
    # 分类与文章的关系是一对多，在多方设置外键
    category = models.ForeignKey(Category)
    # 标签与文章的关系是多对多的关系
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # 为了方便的提取到用户点击的文章信息
        # 自定义一个get_absolute_url
        return reverse('blog:detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-create_time']
