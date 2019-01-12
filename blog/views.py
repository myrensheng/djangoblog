from django.shortcuts import render, get_object_or_404
from markdown import markdown

from blog.models import Post, Category
from comments.form import CommentForm


def index(request):
    # 主页面的视图函数
    post_list = Post.objects.all()
    return render(request,'blog/index.html',context={'post_list':post_list})


def detail(request,pk):
    # 详情页的视图函数
    form = CommentForm()

    post = get_object_or_404(Post,pk=pk)
    post.body = markdown(post.body,extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])
    comment_list = post.comment_set.all()
    context = {'post':post,
               'form':form,
               'comment_list':comment_list,
               }
    return render(request,'blog/detail.html',context=context)

def archives(request,year,month):
    # 归档的视图函数
    post_list = Post.objects.filter(create_time__year=int(year),
                                    create_time__month=int(month),
                                    )
    return render(request,'blog/index.html',context={'post_list':post_list})


def category(request,pk):
    # 分类的视图函数
    cate = get_object_or_404(Category,pk=pk)
    post_list = Post.objects.filter(category=cate)
    return render(request,'blog/index.html',context={'post_list':post_list})