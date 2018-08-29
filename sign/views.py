from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# 主要写处理逻辑


'''
def hello(request):
    if request.method == "GET":
        name = request.GET.get("name")
        if name is None:
            return HttpResponse("请传name")
        else:
            return HttpResponse("hello," + name)
            
'''


# 首页
def index(request):
    return render(request, "index.html")


# 登录处理
def login_action(request):
    if request.method == 'GET':
        username = request.GET.get('username', '')
        password = request.GET.get('password', '')
        if username == '' and password == '':
            return render(request, "index.html", {"error": "用户名或密码为空"})

        if username != "admin" or password != "123":
            return render(request, "index.html", {"error": "用户名或密码错误"})

        else:
            return render(request, "event_manage.html")

