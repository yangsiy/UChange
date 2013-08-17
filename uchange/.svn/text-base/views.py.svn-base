# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, render_to_response
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.core.context_processors import csrf
from django.contrib.auth.models import User

def index(request):
    return render(request,'index.html')

def user_login(request):
    c={}
    c.update(csrf(request))
    username=request.POST['username']
    password=request.POST['password']
    user=authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request,user)
            return HttpResponseRedirect("/home/")
        #return render_to_response('index.html',c)
        else:
            return render_to_response('index.html',c)
    else:
        return render_to_response('index.html',c)

def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/")

def register(request):
    return render(request,'register.html')

def register_operate(request):
    c={}
    c.update(csrf(request))
    username=request.POST['username']
    first_name=request.POST['first_name']
    last_name=request.POST['last_name']
    password=request.POST['password']
    password1=request.POST['password1']
    email=request.POST['email']
    if password!=password1:
        return HttpResponse("Invalid password.")
    user=User.objects.create_user(username,email,password)
    user.first_name=first_name
    user.last_name=last_name
    user.save()
    user=user=authenticate(username=username, password=password)
    login(request,user)
    return HttpResponseRedirect("/home/init")
