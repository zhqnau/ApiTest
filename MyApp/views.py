from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from MyApp.models import *
# Create your views here.


@login_required
def welcome(request):
    print("进来了")
    # return HttpResponse("欢迎来到主页！！！")
    return render(request, "welcome.html", {"key1":1, "key2":2, "key3": [1,2,3]})


@login_required
def api_help(request):
    # print("help")
    return render(request, "welcome.html", {"whichHTML": "help.html", "oid": ""})


def child(request, eid, oid):  # 返回子界面
    # print("list1")
    res = child_json(eid, oid)
    return render(request, eid, res)


def child_json(eid, oid=''):  # 控制不同界面返回不同数据：数据分发器
    res={}
    if eid == 'home.html':
        data = DB_home_href.objects.all()
        res = {"hrefs":data}
    if eid == 'project_list.html':
        data = DB_project.objects.all()
        res = {"projects":data}

    if eid == 'P_apis.html':
        project = DB_project.objects.filter(id=oid)[0]
        apis = DB_apis.objects.filter(project_id=oid)
        res = {"project":project,'apis':apis}
    if eid == 'P_cases.html':
        project = DB_project.objects.filter(id=oid)[0]
        res = {"project": project}
    if eid == 'P_project_set.html':
        project = DB_project.objects.filter(id=oid)[0]
        res = {"project": project}

    return res

# def home(request):
#     return render(request, 'home.html', {"usename":'测试开发'})

@login_required
def home(request):
    return render(request,'welcome.html', {"whichHTML": "home.html", "oid": ""})


def login(request):
    return render(request, 'login.html')


def login_action(request):
    u_name = request.GET['username']  # request 获取用户名密码
    p_word = request.GET['password']
    # print(u_name, p_word)
    # 开始 联通 django 用户库 查看用户名密码是否正确

    from django.contrib import auth
    user = auth.authenticate(username=u_name, password=p_word)

    if user is not None:
        # 进行正确action
        # return HttpResponseRedirect('/home/')
        auth.login(request, user)
        request.session['user'] = u_name
        return HttpResponse('成功')

    else:
        # 返回前端用户名密码错误
        return HttpResponse('失败')


def register_action(request):
    u_name = request.GET['username']  # request 获取用户名密码
    p_word = request.GET['password']
    # print(u_name, p_word)
    # 开始 联通 django 用户库 查看用户名密码是否正确

    from django.contrib.auth.models import User

    try:
        user = User.objects.create_user(username=u_name, password=p_word)
        user.save()
        return HttpResponse('注册成功')
    except:
        return HttpResponse('注册失败-用户已存在')


def logout(request):
    from django.contrib import auth
    auth.logout(request)
    return HttpResponseRedirect('/login/')


def tui(request):
    tui_text = request.GET['tui_text']

    DB_tui.objects.create(user=request.user.username, text=tui_text)

    return HttpResponse('')


@login_required
def project_list(request):
    return render(request,'welcome.html', {"whichHTML": "project_list.html", "oid": ""})


def delete_project(request):
    id = request.GET['id']

    DB_project.objects.filter(id=id).delete()

    return HttpResponse('')


# 新增项目
def add_project(request):
    project_name = request.GET['project_name']
    DB_project.objects.create(name=project_name, remark='', user=request.user.username, other_user='')
    return HttpResponse('')


# 进入接口库
@login_required
def open_apis(request,id):
    project_id = id
    return render(request, 'welcome.html', {"whichHTML":"P_apis.html","oid":project_id})


# 进入用例设置库
@login_required
def open_cases(request,id):
    project_id = id
    return render(request, 'welcome.html', {"whichHTML":"P_cases.html","oid":project_id})


# 进入项目设置
@login_required
def open_project_set(request,id):
    project_id = id
    return render(request, 'welcome.html', {"whichHTML":"P_project_set.html","oid":project_id})


# 新增项目
def save_project_set(request, id):
    project_id = id
    name = request.GET['name']
    remark = request.GET['remark']
    other_user = request.GET['other_user']
    DB_project.objects.filter(id=project_id).update(name=name, remark=remark, other_user=other_user)
    return HttpResponse('')


# 保存备注
def save_bz(request):
    api_id = request.GET['api_id']
    bz_value = request.GET['bz_value']
    DB_apis.objects.filter(id=api_id).update(des=bz_value)
    return HttpResponse('')


# 保存备注
def get_bz(request):
    api_id = request.GET['api_id']
    bz_value = DB_apis.objects.filter(id=api_id)[0].des
    return HttpResponse(bz_value)