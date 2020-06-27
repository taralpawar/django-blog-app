from django.shortcuts import render, HttpResponse, redirect
from .models import Blogs
from django.contrib.auth.models import User, auth
from django.contrib.auth import login, logout
from django.contrib import messages
# Create your views here.


def homepage(request):
    allblogs = Blogs.objects.all()

    return render(request, 'blog/homepage.html', {'allblogs': allblogs})


def newpost(request):
    if request.method == 'POST' and request.FILES['thumbnail']:
        title = request.POST['title']
        body = request.POST['body']
        thumbnail = request.FILES['thumbnail']
        user = request.user
        newblog = Blogs(title=title, body=body,
                        thumbnail=thumbnail, postuser=user)
        newblog.save()

        return redirect('/blog/home')

    else:
        return render(request, 'blog/newpost.html')


def loginuser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login Successfull")
            return redirect('/blog/home')
        else:
            messages.error(
                request, "Please enter correct username and password")
            return redirect('/blog/login')

    else:
        return render(request, 'blog/login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if pass1 == pass2:
            newuser = User.objects.create_user(
                username=username, first_name=fname, last_name=lname, email=email, password=pass1)

            newuser.save()
            return redirect('/blog/home')

    else:
        return render(request, 'blog/register.html')


def logoutuser(request):
    logout(request)
    return redirect('/blog/home')


def readblog(request, id):
    blog = Blogs.objects.get(id=id)
    return render(request, 'blog/readblog.html', {'blog': blog})


def searchblog(request):
    if request.method == 'POST':
        searchtext = request.POST['searchtext']
        if searchtext != '':
            result = Blogs.objects.filter(title__icontains=searchtext)
            return render(request, 'blog/search.html', {'result': result})


def mypost(request):
    user = request.user
    result = Blogs.objects.filter(postuser=user)
    if len(result) > 0:
        return render(request, 'blog/mypost.html', {"result": result})
