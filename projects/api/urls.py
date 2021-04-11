from django.urls import path

from .views import (
    ProjectCreateAPIView,
    ProjectRetriveUpdateDestroyView,
    ProjectListAPIView,
)

app_name = 'project-api'

urlpatterns = [

    path('list', ProjectListAPIView.as_view(), name='list-api'),
    path('<slug:slug>', ProjectRetriveUpdateDestroyView.as_view(), name='detail-api'),
    path('create', ProjectCreateAPIView.as_view(), name='create-api'),

]
