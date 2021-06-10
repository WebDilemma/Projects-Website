from django.shortcuts import render, Http404, get_object_or_404, get_list_or_404, HttpResponse
from django.views.generic import (
    TemplateView,
    DeleteView,
    DetailView,
    CreateView,
    ListView,
    UpdateView,
) 
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import reverse, redirect
from django.contrib.auth.decorators import login_required


from .models import UserProfile
from tags.models import Tag
from projects.models import Project
from . forms import LoginForm, SignUpForm, UserProfileForm



# Create your views here.
def home_view(request):
    return render(request, 'portfolio/home.htm', context={})
    


def profile_detail_view(request, slug):
    instance = get_object_or_404(UserProfile, slug=slug)
    context = {}
    context['object'] = instance
    return render(request, 'portfolio/profile_detail.htm', context=context)

@login_required(login_url='profile:login')
def profile_edit_view(request, slug):
    instance = get_object_or_404(UserProfile, slug=slug)
    context = {}
    profile_form = UserProfileForm(request.POST or None, instance=instance)
    if request.POST:
        if profile_form.is_valid():
            profile_form.save()
            
            return redirect('profile:home')
        
    context['form'] = profile_form
    context['object'] = instance
    return render(request, 'portfolio/profile_edit.htm', context=context)

@login_required(login_url='profile:login')
def profile_delete_view(request, slug):
    instance = get_object_or_404(UserProfile, slug=slug)
    context = {}
    if request.user == instance.user:
        if request.user.is_authenticated and request.POST:
            instance.delete()
            u = User.objects.get(user=request.user)
            u.delete()
            context['delete'] = "once you delete account there is no going back !"
            return redirect('profile:delete-cnf')
    return render(request, 'portfolio/delete_profile.htm', context=context)

def deleted_sucessfuly(request):
    return HttpResponse("Account Deleted Sucsessfuly!")

def login_view(request):
    login_form = LoginForm(request.POST or None)
    context = {}
    if request.method == 'POST':
        if login_form.is_valid():

            username = login_form.cleaned_data.get('username')
            email = login_form.cleaned_data.get('email')
            password = login_form.cleaned_data.get('password')
            
            user = authenticate(username=username, email=email, password=password)
            if user is not None:
                login(request, user)

                return redirect('profile:home')
            
    context['form'] = login_form
    
    return render(request, 'portfolio/login.htm', context=context)
        
             

def signup_view(request):
    signup_form = SignUpForm(request.POST or None)
    context = {}
    if signup_form.is_valid():
        signup_form.save()
        username = signup_form.cleaned_data.get('username')
        email = signup_form.cleaned_data.get('email')
        password = signup_form.cleaned_data.get('password')
        user = authenticate(username=username, email=email, password=password)
        if user is None:
            user = User.objects.create(username=username, email=email)
            user.set_password(password)
            user.save()
            login(request, user)
            return redirect('profile:home')
            
    context['form'] = signup_form
    
    return render(request, 'portfolio/login.htm', context=context)

@login_required(login_url='profile:login')
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('profile:home')
        


