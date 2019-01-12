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
4.# USE_TZ = True,在setting中注释掉这就话，否则在实现归档功能时，会没有文章出现。
使用mysql会出错。参考网站：
https://chowyi.com/Django%E4%BD%BF%E7%94%A8MySQL%E5%90%8E%E7%AB%AF%E6%97%A5%E6%9C%9F%E4%B8%8D%E8%83%BD%E6%8C%89%E6%9C%88%E8%BF%87%E6%BB%A4%E7%9A%84%E9%97%AE%E9%A2%98%E5%8F%8A%E8%A7%A3%E5%86%B3%E6%96%B9%E6%A1%88/
5.models中字段设置blank=True，可以不填该字段
6.在models类中不仅能写字段的类型，还可以定义一个方法匹配到路由。
