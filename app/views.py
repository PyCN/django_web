# -*- encoding:utf8 -*- #
import hashlib
import re
from pandas import json

from django.contrib import auth
from django.contrib.auth import models
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
import models
import forms
from django.template import RequestContext
from django_comments.models import Comment
from django.utils.encoding import smart_str
# Create your views here.


def regist(request):
    errors = []
    if request.method=='POST':
        user=forms.RegistForm(request.POST)
        if user.is_valid():
            username=user.cleaned_data['username']
            email=user.cleaned_data['email']
            password=user.cleaned_data['password']
            password2=user.cleaned_data['password2']
            result= models.BbsUser.objects.filter(user__username=username)
            if len(result)!=1:
                if password==password2:

                    auth.models.User.objects.create(username=username, email=email, password=hashlib.sha1(password))# hashlib.md5也行，sha1更安全，md5更快

                    user=auth.models.User.objects.get(username=username)
                    models.BbsUser.objects.create(user_id=user.id)

                    return HttpResponse('Regist success!,<br><a href="/login/"><u>登陆</u></a>')
                else:
                    errors.append(u'请输入相同的密码')
                    return HttpResponse(u'两次输入的密码不一致!')

            else:
                errors.append(u'用户名已存在')
                return HttpResponse(u'用户名已存在，注册失败')
    else:
        user=forms.RegistForm()
        return render(request,'regist.html',{'user':user})# context_instance


def login(request):

    return render(request,'login.html')


def acct_login(request):

    username=request.POST.get('username')
    password=request.POST.get('password')
    user=auth.authenticate(username=username,password=password)

    if user:
        auth.login(request,user)

        return HttpResponseRedirect('/1/')
    else:
        return render(request,'login.html',{'login_err':u'用户名或密码错误'})


def logout(request):

    auth.logout(request)
    return HttpResponse('logout success!<br><a href="/1/"><u>Home page</u></a>')




def main(request,cate_id):

    models.Category.objects.order_by('id')
    categories=models.Category.objects.all()
    bbs_list=models.Bbs.objects.filter(category__id=cate_id) #category 外键
    return render(request,'bbs.html',{'bbs_list':bbs_list,'category_list':categories,'cate_id':long(cate_id)})


def bbs_content(request,bbs_id):

    categories=models.Category.objects.all()
    bbs=models.Bbs.objects.get(id=bbs_id)
    return render(request,'content.html',{'bbs':bbs,'category_list':categories,})


def sub_comment(request):

    bbs_id=request.POST.get('bbs_id')
    comment=request.POST.get('comment_content',u'评论系统错误，小猜正在赶来修复.....')

    Comment.objects.create(
        content_type_id=8,
        site_id=1,
        user=request.user,
        object_pk=bbs_id,
        comment=comment,
    )
    return HttpResponseRedirect('/content/%s'%bbs_id)


def create_bbs(request):

    content=request.POST.get('content')
    title=request.POST.get('title')
    try:
        username=request.user.username.decode("utf-8") #将unicode格式解码为utf8格式
        author=models.BbsUser.objects.get(user__username=username)   #在前端使用debugtools方法查的request.user属性值是unicode编码方式，而模型中username为utf8
   #author=models.BbsUser.objects.get(user__id=request.user.id)

        source_path=request.META.get('HTTP_REFERER')
        category_num=re.findall(r'/(\d+)/',source_path)[0]

        models.Bbs.objects.create(
            title=title,
            category_id=int(category_num),
            author=author,
            content=content,
            view_count=20,
            ranking=58
        )
        return HttpResponseRedirect('/%s/'%category_num)
    except:
        return HttpResponseRedirect('/login/')

def add_like_num(request):
    bbs_id=request.POST['bbs_id']
    like_num=request.POST["like_num"]
    like_obj=models.Like(
        to_bbs=bbs_id,
        like_num=like_num
    )
    like_obj.save()
    return HttpResponse(json.dumps(like_obj))