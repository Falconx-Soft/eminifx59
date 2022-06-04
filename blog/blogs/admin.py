from django.contrib import admin
from django.shortcuts import render,redirect
from .models import *

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
  

# class CategoryAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'slug': ('Name',)}

admin.site.register(Blog,BlogAdmin)
# admin.site.register(BlogAuthor)
admin.site.register(BlogReply)
admin.site.register(BlogComment)
admin.site.register(contact_us)
admin.site.register(vod)
