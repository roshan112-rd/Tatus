from django.urls import path,include
from. import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path
from django.conf import settings
from django.views.static import serve

urlpatterns = [
	path('',views.home, name='home'),
    path('about/',views.about, name='about'),
    path('blogs/',views.blogs, name='blogs'),
	path('contact/',views.contact, name='contact'),
	path('gallery/',views.gallery, name='gallery'),
    path('projects/',views.projects, name='projects'),
	path('blog_single/<int:id>',views.blog_single, name='blog_single'),
    path('project_single/<int:id>',views.project_single, name='project_single'),
    path('gallery_single/<int:id>',views.gallery_single, name='gallery_single'),
	path('comment/<int:id>',views.comment, name='comment'),
	path('subscribe/',views.subscribe, name='subscribe'),
  

    
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    path('summernote/', include('django_summernote.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)