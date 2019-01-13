from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from markdown import markdown

from blog.models import Post, Category, Tag
from comments.form import CommentForm

# 使用自定义的视图函数完成功能
"""
def index(request):
    # 主页面的视图函数
    post_list = Post.objects.all()
    return render(request,'blog/index.html',context={'post_list':post_list})


def detail(request,pk):
    # 详情页的视图函数
    form = CommentForm()

    post = get_object_or_404(Post,pk=pk)
    #  当该函数调用一次，表示阅读量增加一次
    post.increase_views()
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
"""


# 继承Django自带的类ListView和DetailView类完成功能
# 需要在配置路由的时候使用as_view()函数
class IndexView(ListView):
    model = Post
    content_object_name = 'post_list'
    template_name = 'blog/index.html'
    # django已经将分页器的内容写好，
    # 只需要用paginate_by指定每页的数量
    paginate_by = 2


class CategoryView(IndexView):
    # 获取某个分类下的全部文章
    def get_queryset(self):
        # 路由中传入的参数放到self.kwargs中，用get获取到
        cate = get_object_or_404(Category,pk=self.kwargs.get("pk"))
        # 使用的是父类中的get_queryset()
        return super(CategoryView, self).get_queryset().filter(category=cate)


class ArchivesView(IndexView):
    # 通过创作时间将文章分类
    def get_queryset(self):
        # 路由传过来是是年份和月份
        create_year = self.kwargs.get("year")
        create_month = self.kwargs.get("month")
        return super(ArchivesView, self).get_queryset().filter(create_time__year=create_year,
                                                               create_time__month=create_month)


class PostDetailView(DetailView):
    # 文章详情页的视图类
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'

    def get(self,request,*args,**kwargs):
        # 当每次点击到文章详情页面就将文章的阅读数加1
        response = super(PostDetailView, self).get(request,*args,**kwargs)
        # 将文章的阅读量+1
        self.object.increase_views()
        return response

    def get_object(self, queryset=None):
        # 覆写get_object方法的目的是需要对post的body值进行渲染
        post = super(PostDetailView, self).get_object(queryset=None)
        post.body = markdown(post.body,extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
        ])
        return post

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        form = CommentForm()
        comment_list = self.object.comment_set.all()
        context.update({
            'form':form,
            'comment_list':comment_list,
        })
        return context


class TagView(ListView):
    model = Post
    context_object_name = 'post_list'
    template_name = 'blog/index.html'

    def get_queryset(self):
        tag = get_object_or_404(Tag,pk=self.kwargs.get("pk"))
        return super(TagView, self).get_queryset().filter(tags=tag)