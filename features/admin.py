from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin
admin.site.site_header = "Admin panel"

from django_summernote.models import Attachment

admin.site.unregister(Attachment)


class BlogDate(admin.ModelAdmin):
    list_filter = ('created', )

class Description(SummernoteModelAdmin):
    summernote_fields = ('description',)

class BlogFields(Description, admin.ModelAdmin):
    list_display = ('blog_title', 'created',)

class EventFields(Description, admin.ModelAdmin):
    list_display = ('event_title', 'created',)

class ProjectFields(Description, admin.ModelAdmin):
    list_display = ('project_title', 'created','status')

class ContactFields(admin.ModelAdmin):
    list_display = ('full_name', 'created','contact')

class CommentFields(admin.ModelAdmin):
    list_display = ('full_name', 'created')

class Created(admin.ModelAdmin):
    list_display = ( 'name','created')

class Messages(SummernoteModelAdmin):
    summernote_fields = ('message',)
    
admin.site.register(Blog,BlogFields)
admin.site.register(Contact,ContactFields)
admin.site.register(Event,EventFields)
admin.site.register(Project,ProjectFields)
admin.site.register(Comment,CommentFields)
admin.site.register(Team,Created)
admin.site.register(Testimonial,Created)
admin.site.register(BusinessPartner,Created)
admin.site.register(Message,Messages)
admin.site.register(Subscription)
admin.site.register(Logo)