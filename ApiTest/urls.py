"""ApiTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path

from MyApp.views import *  # 导入后台函数views
# url分发路由管理器
urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^welcome/$', welcome),  # 进入我的主页
    # re_path(r'^case_list/$', list1),  # 进入用例列表
    re_path(r'^home/$', home),  # 进入首页
    re_path(r'^child/(?P<eid>.+)/(?P<oid>.*)/$', child),  # 返回子页面,
    re_path(r'^login/$', login),  # 登录界面
    re_path(r'^login_action/$', login_action),  # 登陆
    re_path(r'^register_action/$', register_action),  # 注册
    re_path(r'^accounts/login/$', login),  # 非登录状态自动跳回登录页面
    re_path(r'^logout/$', logout),  # 注销
    re_path(r'^tui/$', tui),  # 吐槽
    re_path(r'^help/$', api_help),  # 帮助文档
    re_path(r'^project_list/$', project_list),  # 项目列表
    re_path(r'^delete_project/$', delete_project),  # 删除项目
    re_path(r'^add_project/$', add_project),  # 新增项目
    re_path(r'^apis/(?P<id>.*)/$', open_apis),  # 进入接口库
    re_path(r'^cases/(?P<id>.*)/$', open_cases),  # 进入接口库
    re_path(r'^project_set/(?P<id>.*)/$', open_project_set),  # 进入接口库
    re_path(r'^save_project_set/(?P<id>.*)/$', save_project_set),  # 保存项目设置
    re_path(r'^save_bz/$', save_bz),  # 保存备注
    re_path(r'^get_bz/$', get_bz),  # 获取备注

]   # ['url', '后台函数名']
