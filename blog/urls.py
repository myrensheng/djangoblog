from django.conf.urls import url

from blog.views import index, detail


app_name = 'blog'
urlpatterns = [
    url(r'^$', index,name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$',detail,name='detail'),

]
