from django.shortcuts import render, Http404

from django.views.generic import (
    TemplateView,
    DeleteView,
    DetailView,
    CreateView,
    ListView,
    UpdateView,
) 

def contact_us_view(request):
    return render(request, 'contact-us.htm', context={})

class AboutUsView(TemplateView):
    template_name= 'about-us.htm'
    