from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,logout,login
from django.http import HttpResponseRedirect
from forms import RegistrationForm,ProfileForm
from django.core.urlresolvers import reverse


def login_user(request):
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
                return redirect(next_url)

    return render(request,'accounts/login.html',{'username':username,'password':password,'next':next_url})


def logout_user(request):
    logout(request)
    return redirect('core:home')


def sign_up(request):
    if request.method == 'POST':
        registration_form = RegistrationForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if registration_form.is_valid() and profile_form.is_valid():
            user = registration_form.save(commit=False)
            user.save
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
        return HttpResponseRedirect(reverse('core:home'))
    else:
        registration_form = RegistrationForm()
        profile_form = ProfileForm(request.POST)
    return render(request,'core/signup.html',{
        'registration_form':registration_form,
        'profile_form':profile_form
    })
