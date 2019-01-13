from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import redirect
from django.urls import reverse
import markdown
from django.utils.html import strip_tags


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
    views = models.PositiveIntegerField(default=0)

    def save(self,*args,**kwargs):
        #  重写save方法，当自动生成文章的摘要显示在index网页中
        if not self.excerpt:
            md = markdown.Markdown(extensions=[
                    'markdown.extensions.extra',
                    'markdown.extensions.codehilite',
                ])
            self.excerpt = strip_tags(md.convert(self.body))[:54]
        #  调用父类的save方法，将数据存储到数据库
        super(Post, self).save(*args,**kwargs)

    def increase_views(self):
        # 文章浏览一次，数据库中的views字段就加一
        self.views += 1
        self.save(update_fields=['views'])

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # 为了方便的提取到用户点击的文章信息
        # 自定义一个get_absolute_url
        return reverse('blog:detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-create_time']
