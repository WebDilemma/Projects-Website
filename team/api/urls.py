from django.urls import path

from .views import (
    TeamListAPIView,
    team_profile_delete_api_view,
    team_profile_retirve_api_view,
    TeamProfileUpdateAPIView
)

app_name = 'team-api'

urlpatterns = [

    path('list/', TeamListAPIView.as_view(), name='list-api'),
    path('<int:pk>/', team_profile_retirve_api_view, name='detail-api'),
    path('<int:pk>/delete', team_profile_delete_api_view, name='delete-api'),
    path('<int:pk>/update', TeamProfileUpdateAPIView.as_view(), name='update-api'),
    
]