from django.shortcuts import render

from django.shortcuts import render, Http404
from django.views.generic import (
    TemplateView,
    DeleteView,
    DetailView,
    CreateView,
    ListView,
    UpdateView,
) 

from django.contrib.auth.models import User

from portfolio.models import UserProfile
from tags.models import Tag
from projects.models import Project
from django.contrib.auth.mixins import PermissionRequiredMixin
# Create your views here.


class ProjectCreateView(PermissionRequiredMixin, CreateView):
    model = Project
    template_name = 'projects/project_create.htm'
    fields = ['title', 'img', 'text', 'categorie', 'link', 'tools', 'author']
    permission_required = ('projects.delete_project')
    success_url = '/'

class ProjectUpdateView(UpdateView):
    model = Project
    template_name_suffix = '_update_form'
    fields = ['title', 'img', 'text', 'categorie', 'link', 'tools']
    success_url = '/' 

class ProjectListView(ListView):
    model = Project
    template_name = "projects/project_list.htm"
    
    def get_queryset(self, **kwargs):
        context = super().get_queryset(**kwargs)
        
        return context
    
class ProjectDetailView(DetailView):
    model = Project
    find_by = 'slug'
    slug_url_kwarg = 'slug'
    template_name = 'projects/project_detail.htm'
    
    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'projects/project_confirm_delete.htm'


class SearchProject(ListView):
    pass