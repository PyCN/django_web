"""bbs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.contrib import admin
from django.conf.urls import include, url

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^(\d+)/$','app.views.main',name='index'),
    url(r'^content/(\d+)/$','app.views.bbs_content',name='content'),
    url(r'^comment/$','app.views.sub_comment',name="comment"),


    url(r'^login/$','app.views.login', name="login"),
    url(r'^acct_login/$','app.views.acct_login',name="acct_login"),
    url(r'^regist/$','app.views.regist',name='regist'),
    url(r'^logout/$','app.views.logout',name="logout"),
    url(r'^create/$','app.views.create_bbs',name='create'),

    url(r'^add_like_num/','app.views.add_like_num',name='add_like_num')

]
