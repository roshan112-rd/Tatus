from django.db import models
from django.contrib import admin
from django.db import models
from PIL import Image

# Create your models here.
class Blog(models.Model):
    blog_title = models.CharField(max_length=1000)
    description = models.TextField()
    tags = models.CharField(max_length=500, default='')
    image = models.ImageField(null=True, upload_to='blog_images/' )
    created = models.DateTimeField(auto_now_add=True, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        output_size = (720, 389)
        img.thumbnail(output_size)
        img.save(self.image.path)
        
    def __str__(self):
        return self.blog_title



class Contact(models.Model):
    full_name = models.CharField(max_length=1000,null=True)
    email = models.CharField(max_length=1000, null=True)
    contact = models .IntegerField()
    message = models .TextField()
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.full_name


class Event(models.Model):
    event_id = models.AutoField(primary_key=True, null=False)
    event_title = models.CharField(max_length=1000,null=True)
    description = models.TextField()
    start_date = models.DateField(max_length=1000,null=True)
    end_date = models.DateField(max_length=1000,null=True)
    image1 = models.ImageField(null=True, upload_to='event_images/')
    image2 = models.ImageField(null=True, upload_to='event_images/')
    created = models.DateTimeField(auto_now_add=True, null=True)



    def __str__(self):
        return self.event_title


class Project(models.Model):
    project_id = models.AutoField(primary_key=True, null=False)
    STATUS_CHOICES = (
        ('ongoing', 'ongoing'),
        ('upcoming', 'upcoming'),
        ('completed', 'completed'),
    )
    project_title = models.CharField(max_length=1000,null=True)
    status = models.CharField(max_length=250, choices=STATUS_CHOICES, default='completed')
    description = models.TextField()
    start_date = models.DateField(max_length=1000,null=True)
    image1 = models.ImageField(null=True, upload_to='project_images/')
    image2 = models.ImageField( null=True, upload_to='project_images/')
    end_date = models.DateField(max_length=1000,null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return self.project_title



class Team(models.Model):
    name= models.CharField(max_length=100, null=True)
    designation = models.CharField(max_length=100)
    image =models.ImageField(upload_to='team_images/', null=True)
    facebook = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.designation



class Testimonial(models.Model):
    name= models.CharField(max_length=1000)
    address= models.CharField(max_length=1000)
    image = models.ImageField( null=True, upload_to='testimonial_images/' )
    testimonial= models.TextField()
    created = models.DateTimeField(auto_now_add=True, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name



class Comment(models.Model):
    blog= models.ForeignKey(Blog, on_delete=models.CASCADE, null=True)
    full_name = models.CharField(max_length=1000, null=True)
    email = models.CharField(max_length=1000, null=True)
    comment = models.CharField(max_length=1000, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return self.full_name

class BusinessPartner(models.Model):
    name= models.CharField(max_length=100)
    image = models.ImageField(null=True, upload_to='business_partner_images' )
    created = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.name


class Message(models.Model):
    name= models.CharField(max_length=100, null=True)
    designation = models.CharField(max_length=100, null=True)
    message = models.TextField()
    image = models.ImageField(null=True, upload_to='team_images' )
    created = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.name