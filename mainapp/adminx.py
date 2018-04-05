"""
    @Time: 2018/4/5 16:42
    @Author:fangDD
"""
import xadmin
from xadmin import views


class GlobalSetting(object):
    site_title = 'OSPsinspur'
    site_footer = 'PS社区'


xadmin.site.register(views.CommAdminView, GlobalSetting)