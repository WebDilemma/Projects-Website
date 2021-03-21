from django.urls import path


from .views import (
    ProjectCreateView, 
    ProjectDeleteView, 
    ProjectDetailView,
    ProjectEditView,
    ProjectListView,
)
    

app_name="projects"

urlpatterns = [
    path('create/', ProjectCreateView.as_view(), name='create'),
    path('<slug:slug>/delete', ProjectDeleteView.as_view(), name='delete'),
    path('<slug:slug>', ProjectDetailView.as_view(), name='detail'),
    path('<slug>/edit', ProjectEditView.as_view(), name='edit'),
    path('list', ProjectListView.as_view, name='list'),
]
