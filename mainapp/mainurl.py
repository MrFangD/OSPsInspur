"""
    @Time: 2018/4/5 16:28
    @Author:fangDD
"""
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    ]