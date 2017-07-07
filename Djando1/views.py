from django.shortcuts import render
from django.shortcuts import redirect
from Djando1 import models

from django.shortcuts import HttpResponse

from django.conf import settings
from django.core.mail import EmailMultiAlternatives

from_email = settings.DEFAULT_FROM_EMAIL
# Create your views here.

def index(request):
    # return HttpResponse('hello')
    # return render(request,"index.html")
    if request.method == 'GET':
        username = request.POST.get("username", None)
        pwd = request.POST.get("pwd", None)
        # print(username,pwd)

    user_list = models.UserInfo.objects.all()
    return render(request, "index.html", {"data":user_list})

def sign(request):
    if request.method == 'POST':
        username = request.POST.get("username", None)
        pwd = request.POST.get("pwd", None)
        models.UserInfo.objects.create(user=username, pwd=pwd)
        return redirect("/index", )
    else: return render(request, "sign.html", )

def position(request):
    # if request.method == 'POST':
    #     username = request.POST.get("username", None)
    #     pwd = request.POST.get("pwd", None)
    #     models.UserInfo.objects.create(user=username, pwd=pwd)
    #     return redirect("/index", )
    # else:
    return render(request, "position.html", )
def add(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))
def myemail(request):

    # subject 主题 content 内容 to_addr 是一个列表，发送给哪些人
    subject = "title"
    content = "content"
    to_addr = "yunkai3322@163.com"
    msg = EmailMultiAlternatives(subject, content, from_email, [to_addr])

    msg.content_subtype = "text"

    # 添加附件（可选）
    # msg.attach_file('./twz.pdf')

    # 发送
    msg.send()
    return HttpResponse("success")