from blog.models import Post, Category
from django import template

register = template.Library()


@register.simple_tag
def get_recent_posts(num=5):
    # 获取到最新的5篇文章
    return Post.objects.all()[:num]


@register.simple_tag
def archives():
    return Post.objects.dates('create_time','month',order='DESC')


@register.simple_tag
def get_categories():
    return Category.objects.all()
