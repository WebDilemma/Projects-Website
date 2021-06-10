from django.shortcuts import render

from .models import OurTeam
from .forms import TeamForm



# Create your views here.
def add_to_team(request):
    context = {}
    team_form = TeamForm(request.POST or None)
    context['form'] = team_form
    if request.POST:
        if request.user.is_staff and request.user.is_authenticated:
           
            context['form'] = team_form
            team_form.save()
            
    return render(request, 'teams/add-edit-team.html', context=context)
            
            
def edit_team_member(request, username):
    context = {}
    user = request.user
    team_form = TeamForm(request.POST or None, instance=user)
    context['form'] = team_form
    if request.POST:
        if request.user.is_staff and request.user.is_authenticated:
           
            context['form'] = team_form
            team_form.save()
            
    return render(request, 'teams/add-edit-team.html', context=context)
            

def team_list(request):
    team = OurTeam.objects.all(active=True)