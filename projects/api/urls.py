from django.urls import path

from .views import (
    ProjectCreateAPIView,
    project_retirve_api_view,
    project_delete_api_view,
    ProjectUpdateAPIView,
    ProjectListAPIView,
)

app_name = 'project-api'

urlpatterns = [

    path('list/', ProjectListAPIView.as_view(), name='list-api'),
    path('create/', ProjectCreateAPIView.as_view(), name='create-api'),
    path('<slug:slug>/', project_retirve_api_view, name='detail-api'),
    path('update/<slug:slug>', ProjectUpdateAPIView.as_view(), name='update-api'),
    path('delete/<slug:slug>', project_delete_api_view, name='delete-api'),

]
