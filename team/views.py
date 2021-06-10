from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required, permission_required

from .models import OurTeam
from .forms import TeamForm



# Create your views here.
@login_required(login_url='profile:login')
def add_to_team(request):
    context = {}
    team_form = TeamForm(request.POST or None)
    context['form'] = team_form
    if request.POST:
        if request.user.is_staff and request.user.is_authenticated:
           if team_form.is_valid():
                context['form'] = team_form
                team_form.save()
                return redirect('team:home')
            
    return render(request, 'team/add-edit-team.html', context=context)


            
@login_required(login_url='profile:login')          
def edit_team_member(request, slug):
    context = {}
    user = request.user
    try:
        team_user = OurTeam.objects.get(slug=slug)
    except:
        team_user = None
    team_form = TeamForm(request.POST or None, instance=user)
    context['form'] = team_form
    if request.POST:
        if request.user.is_staff and request.user.is_authenticated:
           if team_form.is_valid():
                context['form'] = team_form
                team_form.save()
                return reverse('team:profile', kwargs={'slug':slug})
            
    return render(request, 'team/add-edit-team.html', context=context)
            

def team_list(request):
    context = {}
    try:
        team = OurTeam.objects.all(active=True)
    except:
        team = None
    context['objects_list'] = team
    return render(request, 'team/teams.html', context=context)


def team_profile(request, slug):
    context = {}
    try:
        team_profile = OurTeam.objects.get(slug=slug)
    except:
        team_profile = None
        
    context['object'] = team_profile
    
    return render(request, 'team/detail.html', context=context)

def team_profile_delete(request, slug):
    if request.user.is_authenticated and request.user.is_staff:
        if request.method == 'POST':
            try:
                obj  = OurTeam.objects.get(slug=slug)
                obj.delete()
            except:
                pass
            return redirect('team:home')