from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [

    path('',views.BlogList,name='list'),
    url(r'^detail/(?P<slug>[-\w]+)$',views.BlogDetail,name='detail'),
    url(r'^search/',views.search,name='search'),
    url(r'^blog/',views.blogFormView,name='blog'),
    url(r'^reply/(?P<id>\d+)/(?P<slug>[-\w]+)/$',views.ReplyPage,name='reply'),
    path('comment_reply/', views.comment_reply, name="comment_reply"),
    path('about_us/', views.about_us, name="about_us"),
    path('blogs/', views.blogs, name="blogs"),
    path('vod/', views.vod_function, name="vod"),
    path('contact-us/', views.contactUs, name="contact_us"),
    path('terms/', views.terms, name="terms")


####################################################################################################



    # url(r'^authorlist/',views.BlogAuthors,name='authorlist'),    
    # url(r'^author/(?P<id>\d+)$', views.BlogListByAuthor, name="blog-by-author"),
    # # url(r'^category/(?P<slug>[-\w]+)/$', views.base, name='category'),
    # # url(r'^cat/', views.base1, name='cat'),
    # # url(r'^subscribe/',views.sub,name='subscribe'),
    # # url(r'^contact/',views.Contact,name='contact'),


]