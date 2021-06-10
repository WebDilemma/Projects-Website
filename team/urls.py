from django.urls import path

from . views import (
    team_list, 
    add_to_team,
    edit_team_member,
    team_profile,
    team_profile_delete
)

app_name = 'team'

urlpatterns = [
    path('', team_list, name='home'),
    path('add_member', add_to_team, name='add'),
    path('<slug>', team_profile, name='detail'), 
    path('<slug>/edit', edit_team_member, name='edit-profile'),
    path('<slug>/delete', team_profile_delete, name='delete-profile'),
    
]