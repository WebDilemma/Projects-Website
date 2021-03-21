from django.urls import path


from .views import (
    home_view,
    
    profile_delete_view,
    deleted_sucessfuly,
    profile_detail_view, 
    profile_edit_view, 
    
    signup_view,
    login_view, 
    logout_view,
)
    

app_name="profile"

urlpatterns = [
    path('', home_view, name='home'),

    path('profile/<slug:slug>/delete/', profile_delete_view, name='delete'),
    path('profile/<slug:slug>', profile_detail_view, name='detail'),
    path('profile/<slug:slug>/edit/', profile_edit_view, name='edit'),
    
    path('profile/deleted', deleted_sucessfuly, name='delete-cnf'),
    path('logout/', logout_view, name='logout'),
    path('sign-up/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    
]

