"""
    @Time: 2018/4/5 16:28
    @Author:fangDD
"""
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^help/$', views.help, name='help'),
    ]