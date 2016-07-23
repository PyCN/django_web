# -*- encoding:utf8 -*-
from django.contrib import admin
from models import Bbs,Category,BbsUser
# Register your models here.


class BbsAdmin(admin.ModelAdmin):
    list_display=('title','get_username','view_count','create_at')   #get_list_display函数可定制针对不同用户不同显示页面
    search_fields=('title','author__user__username')
    date_hierarchy='create_at'
    ording=('-create_at',)
    list_filter=('create_at',)

    def get_username(self, obj):
        return obj.author.user.username
    get_username.short_description='author2'


class BbsUserAdmin(admin.ModelAdmin):
    list_display=('user','signature',)
    search_fields=('user',)
    list_display_links=('user',)


admin.site.register(Bbs,BbsAdmin)
admin.site.register(Category)
admin.site.register(BbsUser,BbsUserAdmin)