from multiprocessing import context
from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings
from django.core.mail import send_mail
from .tokens import account_activation_token
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.defaultfilters import slugify



def base(request, slug):
    categories = Category.objects.get(slug=slug)
    lists = Blog.objects.all()
    blogs = Blog.objects.filter(catagory=categories)
    print(blogs)
    context = {
        'blogs':blogs,
        'list':lists
    }
    return render(request, 'category.html', context)
def base1(request):
    categories = Category.objects.all()
 
    
    context = {
        'cat':categories
    }
    return render(request, 'base.html', context)

def BlogList(request):
    blog = Blog.objects.all()

    recommended_blog = Blog.objects.filter(recommended=True)

    paginator = Paginator(blog ,2) # Shows only 10 records per page

    page = request.GET.get('page')
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
    # If page is not an integer, deliver first page.
        blogs = paginator.page(1)
    except EmptyPage:
    # If page is out of range (e.g. 7777), deliver last page of results.
        blogs = paginator.page(paginator.num_pages)
        
    for i in (blogs):
        i.description=i.description[:500]
    context = {
        'blogs':blogs,
        'blog':blog,
        'recommended_blog':recommended_blog
    }
    return render(request,'home.html',context)

def BlogDetail(request,slug):
    lis   = Blog.objects.all()
    blogs = Blog.objects.get(slug=slug)
    comments= BlogComment.objects.filter(blog=blogs)
    # reply = BlogReply.objects.filter(comment = comments)    
    # print(reply)
    replies = BlogReply.objects.all()
    # print(comments)
    form = Comment()
    form_1 = Reply()
    if request.method =='POST':
         form=Comment(request.POST or None)
         if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.blog=blogs
            new_comment.save()
            form.save()
            return HttpResponseRedirect(reverse('detail', args=[slug]))
             
 
    context = {
        'blogs':blogs,
        'comments':comments,
        'list':lis,
        'form':form,
        # 'relpy' : reply,
        'replies' : replies,
        'form_1' : form_1,
    }
    return render(request,'details.html',context)

def search(request):

    query=request.GET.get('query',None)
    blogs=Blog.objects.all()
    if query is not None:
        blogs=blogs.filter(
        Q(title__icontains=query)|
        Q(description__icontains=query)|
        Q(author__username__icontains=query)

        )
    context={

        'blogs':blogs
}

    return render(request,'search-blog.html',context)

def ReplyPage(request,id, slug):
    comment=BlogComment.objects.get(id=id)
    form = Reply()
    if request.method=='POST':
        form = Reply(request.POST or None)
        if form.is_valid:
            new = form.save(commit=False)
            new.comment=comment
            new.save()
            form.save()
            return HttpResponseRedirect(reverse('detail', args = [slug]))
                
    context={
    #'reply': reply,
    'form1':form,
    'comment': comment,
    'slug' : slug,
    }
    return render(request,'blogReply.html',context)

def comment_reply(request):
    if request.method=='POST':
        form = Reply(request.POST or None)
        if form.is_valid:
            id = request.POST.get('blog_id')
            slug = request.POST.get('blog_slug')
            comment=BlogComment.objects.get(id=id)
            new = form.save(commit=False)
            new.comment=comment
            new.save()
            form.save()
            return HttpResponseRedirect(reverse('detail', args = [slug]))



def blogFormView(request):
    form = blogform()
    if request.method=='POST':
        form = blogform(request.POST ,  request.FILES)
        if form.is_valid():
            new = form.save(commit=False)
            new.author=request.user
            new.slug=slugify(new.title)
            new.save()
            form.save()
            return redirect('list')
                
    context={
    #'reply': reply,
    'form':form,

    }
    return render(request,'blogform.html',context)


def about_us(request):
    return render(request,'about-us.html')

def blogs(request):
    blog = Blog.objects.all()

    recommended_blog = Blog.objects.filter(recommended=True)

    paginator = Paginator(blog ,2) # Shows only 10 records per page

    page = request.GET.get('page')
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
    # If page is not an integer, deliver first page.
        blogs = paginator.page(1)
    except EmptyPage:
    # If page is out of range (e.g. 7777), deliver last page of results.
        blogs = paginator.page(paginator.num_pages)
        
    for i in (blogs):
        i.description=i.description[:500]
    context = {
        'blogs':blogs,
        'blog':blog,
        'recommended_blog':recommended_blog
    }
    return render(request,'blogs.html',context)

def vod_function(request):
    vod_all = vod.objects.all()


    paginator = Paginator(vod_all ,5) # Shows only 10 records per page

    page = request.GET.get('page')
    try:
        vod_obj = paginator.page(page)
    except PageNotAnInteger:
    # If page is not an integer, deliver first page.
        vod_obj = paginator.page(1)
    except EmptyPage:
    # If page is out of range (e.g. 7777), deliver last page of results.
        vod_obj = paginator.page(paginator.num_pages)


    context = {
        'vod_obj':vod_obj
    }
    return render(request,'vod.html',context)


def contactUs(request):

    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact_us_obj = contact_us.objects.create(name=name,email=email,message=message)
        contact_us_obj.save()
    return render(request,'contact-us.html')


def terms(request):
    return render(request,'terms.html')

def home_video(request):
    intro_obj = intro.objects.all()
    context = {
        'intro_obj':intro_obj
    }
    return render(request,'home_video.html',context)