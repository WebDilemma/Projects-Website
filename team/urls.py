from django.urls import path

from . views import (
    teams_list, 
    add_to_team,
    edit_team_member,
    team_profile,
    team_profile_delete
)

app_name = 'team'

urlpatterns = [
    path('', teams_list, name='home'),
    path('add-member', add_to_team, name='add'),
    path('<slug>', team_profile, name='detail'), 
    path('<slug>/edit', edit_team_member, name='edit-profile'),
    path('<slug>/delete', team_profile_delete, name='delete-profile'),
    
]