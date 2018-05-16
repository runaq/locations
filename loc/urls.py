from django.conf.urls import include, url
from . import views


urlpatterns =[ 
    url(r'^$', views.post_list, name='post_list'),
    url(r'^new/$', views.post_new, name='post_new'),
    url(r'^(?P<pk>\d+)/$', views.post_edit, name='post_edit'),
    url(r'^(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
]
