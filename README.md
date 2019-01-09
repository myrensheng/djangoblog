# djangoblog
参考写一个django博客网站
1.使用数据库的时候，安装mysqlclient报错，使用whl文件安装

2.在存储时间的时候，
~~~
TIME_ZONE = 'Asia/Shanghai'，USE_TZ = True，
~~~
尽管在数据库中存储的时间少了8个小时，
但在模板上显示的是正确的。
3.django的站点管理
```(python)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','create_time','modified_time','category','author']
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
```