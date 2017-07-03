from django.shortcuts import render
from Djando1 import models

from django.shortcuts import HttpResponse

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
        return render(request, "index.html", )
    else: return render(request, "sign.html", )