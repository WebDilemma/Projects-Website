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

# Create your views here.


class ProjectCreateView(CreateView):
    model = Project
    template_name = 'projects/project_create.htm'
    fields = ['title', 'img', 'text', 'categorie', 'link', 'tools']
    success_url = '/'
    

class ProjectListView(ListView):
    model = Project
    template_name = "projects/project_list.htm"
    paginate_by = 9
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = None
        return context
    
class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/project_detail.htm'

class ProjectEditView(UpdateView):
    model = Project
    template_name = 'projects/project_create.htm'
    fields = ['title', 'img', 'text', 'categorie', 'link', 'tools']
    success_url = '/'

class ProjectDeleteView(DeleteView):
    model = Project



class SearchProject(ListView):
    pass