from django.conf.urls import url
from .import views


urlpatterns =[
url(r'^$', views.index, name='index'),
url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
url(r'^post/(?P<pk>\d+)/comment/$',views.add_comment, name='add_comment')
]