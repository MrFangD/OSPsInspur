"""
    @Time: 2018/4/5 16:42
    @Author:fangDD
"""
import xadmin
from xadmin import views
from .models import Area


class Area1(object):
    list_display = ['id', 'name', 'parent_area', 'community', 'level']
    list_filter = ['name']
    search_filter = ['name']


class GlobalSetting(object):
    site_title = 'OSPsinspur'
    site_footer = 'PS社区'


xadmin.site.register(Area, Area1)
xadmin.site.register(views.CommAdminView, GlobalSetting)