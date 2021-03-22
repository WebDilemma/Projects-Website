from django.urls import path


from .views import (
    ProjectCreateView, 
    ProjectDeleteView, 
    ProjectDetailView,
    ProjectListView,
    ProjectUpdateView,
)
    

app_name="projects"

urlpatterns = [
    path('create', ProjectCreateView.as_view(), name='create'),
    path('<slug:slug>/delete', ProjectDeleteView.as_view(), name='delete'),
    path('<slug:slug>/update', ProjectUpdateView.as_view(), name='update'),
    path('<slug:slug>', ProjectDetailView.as_view(), name='detail'),
    path('', ProjectListView.as_view(), name='list'),
]
