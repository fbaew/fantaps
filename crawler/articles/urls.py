from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^all$', views.index, name='index'),
    url(r'^(?P<article_id>\d.*)$', views.article_text, name='article_text'),
    url(r'^tag/(?P<tag_name>\w.*)$',views.tag_roundup, name='tag_roundup')
]