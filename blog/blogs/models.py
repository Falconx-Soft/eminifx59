from operator import mod
from pydoc import describe
from django.db import models
from django.conf import settings
from embed_video.fields import EmbedVideoField
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.conf import settings
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

class Blog(models.Model):
    author      =       models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title       =       models.CharField(max_length=1000) #d
    slug        =       models.CharField(max_length=1000)
    image       =       models.ImageField(blank=True)
    video       =       EmbedVideoField(blank=True)
    description =       RichTextUploadingField() #d
    created_at  =       models.DateTimeField(auto_now_add=True) #d
    updated     =       models.DateTimeField(auto_now=True)
    publish     =       models.BooleanField(blank=True,default=False)
    recommended =       models.BooleanField(default=False)
    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title




class BlogComment(models.Model):
    name        =       models.CharField(max_length=100)
    email       =       models.CharField(max_length=100)
    description =       models.TextField(max_length=1000)
    post_date   =       models.DateTimeField(auto_now_add=True)
    blog        =       models.ForeignKey(Blog, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-post_date"]

    def __str__(self):
        return self.description
    
  



class BlogReply(models.Model):
    name        =       models.CharField(max_length=100)
    email       =       models.CharField(max_length=100)
    description =       models.TextField(max_length=1000)
    post_date   =       models.DateTimeField(auto_now_add=True)
    comment     =       models.ForeignKey(BlogComment, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-post_date"]

    def __str__(self):
        return self.name

    
class contact_us(models.Model):
    name        =       models.CharField(max_length=100)
    email       =       models.CharField(max_length=100)
    message     =       models.TextField(max_length=1000)

    def __str__(self):
        return self.name
    
class vod(models.Model):
    name        =       models.CharField(max_length=100)
    created_at  =       models.DateTimeField(auto_now_add=True)
    video       =       EmbedVideoField()
    describe    =       models.TextField(max_length=1000, null=True)

    def __str__(self):
        return self.name