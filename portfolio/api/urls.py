from django.urls import path

from .views import (
    ProfileListAPIView,
    profile_retirve_api_view,
    profile_delete_api_view,
    ProfileUpdateAPIView,
)

app_name = 'profile-api'

urlpatterns = [

    path('list/', ProfileListAPIView.as_view(), name='list-api'),
    path('<slug:slug>/', profile_retirve_api_view, name='detail-api'),
    path('delete/', profile_delete_api_view, name='delete-api'),
    path('update/', ProfileUpdateAPIView.as_view(), name='delete-api'),

]
