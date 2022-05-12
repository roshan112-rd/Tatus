from operator import contains
from django import shortcuts
from django.shortcuts import render,redirect
from .models import *
from django.core.paginator import Paginator
from django.shortcuts import render


#homepage views
def home(request):
    project = Project.objects.all()
    if project:
        paginator = Paginator(project, 3)
        page = request.GET.get('page')
        project = paginator.get_page(page)
    testimonial = Testimonial.objects.all()

    team=Team.objects.all()
    if team:
        paginator = Paginator(team, 4)
        page = request.GET.get('page')
        team = paginator.get_page(page)
    
    blog=Blog.objects.all()
    if blog:
        paginator = Paginator(blog, 3)
        page = request.GET.get('page')
        blog = paginator.get_page(page)
    header_logo=Logo.objects.all()
    footer_logo=Logo.objects.all()
    return render(request,'home.html', {'project': project, 'testimonial':testimonial, 'team':team,'blog':blog, 'header_logo': header_logo, 'footer_logo': footer_logo})



#About page views
def about(request):
    team = Team.objects.all()
    if team:
        paginator = Paginator(team, 4)
        page = request.GET.get('page')
        team = paginator.get_page(page)

        
    testimonial = Testimonial.objects.all()
    if testimonial:
        paginator = Paginator(testimonial, 2)
        page = request.GET.get('page')
        testimonial = paginator.get_page(page)

    partner = BusinessPartner.objects.all()

    header_logo=Logo.objects.all()
    footer_logo=Logo.objects.all()
    message = Message.objects.all().order_by('-created')
    count=message.count()
    if(count == 1):  
        message1 = message[0]
        print('count1')
        return render(request,'about.html', {'team':team, 'testimonial':testimonial, 'partner':partner, 'message1':message1, 'header_logo': header_logo, 'footer_logo': footer_logo})
       
    elif(count >= 2):
        message1 = message[0]
        message2 = message[1]
        print('count2')
        return render(request,'about.html', {'team':team, 'testimonial':testimonial, 'partner':partner, 'message1':message1, 'message2':message2, 'header_logo': header_logo, 'footer_logo': footer_logo})
    else:
        print('count3')
        return render(request,'about.html', {'team':team, 'testimonial':testimonial, 'partner':partner, 'header_logo': header_logo, 'footer_logo': footer_logo})
        
    


def blogs (request):
    header_logo=Logo.objects.all()
    footer_logo=Logo.objects.all()
    blog=Blog.objects.all()
    return render(request,'blogs.html',{'blog':blog, 'header_logo': header_logo, 'footer_logo': footer_logo})


def blog_single (request, id):
    header_logo=Logo.objects.all()
    footer_logo=Logo.objects.all()
    blog=Blog.objects.get(id= id)
    comment=Comment.objects.filter(blog_id=id)
    return render(request,'blog_single.html',{'blog':blog, 'comment':comment,'header_logo': header_logo, 'footer_logo': footer_logo})


def comment(request,id):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
        comment = request.POST['comment']
        
        Comment.objects.create(full_name=full_name, email=email,comment=comment,blog=Blog.objects.get(id=id))
        return redirect ('blog_single',id)
    return redirect('blog_single')


def contact(request):
    header_logo=Logo.objects.all()
    footer_logo=Logo.objects.all()
    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
        message = request.POST['message']
        Contact.objects.create(full_name=full_name, email=email, message=message,contact=contact)
        return redirect ('home')
    return render (request,'contact.html', {'header_logo': header_logo, 'footer_logo': footer_logo})


def events (request):
    header_logo=Logo.objects.all()
    footer_logo=Logo.objects.all()
    event= Event.objects.all()
    return render(request, 'events.html', {'event':event, 'header_logo': header_logo, 'footer_logo': footer_logo})


def event_single (request, id):
    header_logo=Logo.objects.all()
    footer_logo=Logo.objects.all()
    event=Event.objects.get(event_id= id)
    return render(request,'event_single.html',{'event':event, 'header_logo': header_logo, 'footer_logo': footer_logo})


def projects (request):
    header_logo=Logo.objects.all()
    footer_logo=Logo.objects.all()
    completed = Project.objects.filter(status = "completed")
    ongoing = Project.objects.filter(status = "ongoing")
    upcoming = Project.objects.filter(status = "upcoming")
    return render(request, 'projects.html', {'completed': completed,'ongoing': ongoing,'upcoming': upcoming, 'header_logo': header_logo, 'footer_logo': footer_logo})


def project_single (request, id):
    header_logo=Logo.objects.all()
    footer_logo=Logo.objects.all()
    project=Project.objects.get(project_id= id)
    return render(request,'project_single.html',{'project':project,'header_logo': header_logo, 'footer_logo': footer_logo})


def error(request,exception):
    return render (request, '404.html')


def subscribe(request):
    
    if request.method == 'POST':
        email = request.POST['email']
        Subscription.objects.create(email=email)
        return redirect ('home')
    return render (request,'contact.html')