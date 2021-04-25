from django.contrib import admin
from MyApp.models import *
# Register your models here.
# 管理Django后台文件。所有后台数据库表要再此注册


admin.site.register(DB_tui)
admin.site.register(DB_home_href)
admin.site.register(DB_project)

admin.site.register(DB_apis)