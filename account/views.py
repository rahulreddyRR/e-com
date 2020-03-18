from django.shortcuts import render
from django.contrib.auth import login,logout,authenticate
from account.forms import Userregisterform
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def check(request):
    return render(request,'base.html')

def usereg(request):
    if request.method =="POST":
        userdetails = Userregisterform(data=request.POST)
        if userdetails.is_valid():
            user=userdetails.save()
            login(request,user)
            return HttpResponseRedirect(reverse('check'))
        else:
            print(userdetails.errors)

    userregister = Userregisterform()
    return render(request,'account/register.html',{'register':userregister})

def loginview(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username,password = password)
        if user.is_active:
            login(request,user)
            return HttpResponseRedirect(reverse('check'))
        else:
            return render(request,'account/login.html')
    return render(request,'account/login.html')

@login_required
def logoutuser(request):
    logout(request)
    return HttpResponseRedirect(reverse('check'))
