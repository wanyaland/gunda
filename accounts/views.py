from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,logout,login
from django.http import HttpResponseRedirect


def login(request):
    username=password=''
    next_url=''
    if request.GET:
        next_url = request.GET.get('next')
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        next_url = request.POST.get('next')
        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(next_url)
    return render(request,'accounts/login.html',{'username':username,'password':password,'next':next_url})


def logout(request):
    logout(request)
    return redirect('core:home')
