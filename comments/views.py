from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from blog.models import Post
from comments.form import CommentForm


def post_comment(request,post_pk):
    # 获取用户评论的文章
    post = get_object_or_404(Post,pk=post_pk)
    if request.method == "POST":
        # 用户提交的数据存在request.POST中，这是一个列字典对象
        # 利用用户提交的数据创建一个表单对象
        form = CommentForm(request.POST)
        # 使用这个form对象来验证提交的数据是否合法
        if form.is_valid():
            # 如果数据是合法的，调用表单的save方法
            # 将评论数据存到数据库,commit=False表示利用表单的数据生成
            # Comment模型对象，但还不保存评论数据到数据库
            comment = form.save(commit=False)
            # 将评论与被评论的文章关联起来
            comment.post = post
            # 将评论数据保存到数据库
            comment.save()
            # 重定向到Post类中的get_absolute_url方法返回URL
            return redirect(post)
        else:
            # 通过post反向查询到评论
            comment_list = post.comment_set.all()
            context = {
                'post':post,
                'form':form,
                'comment_list':comment_list,
            }
            return render(request,'blog/detail.html',context=context)
    return redirect(post)

