from django.shortcuts import render, Http404

from django.views.generic import (
    TemplateView,
    DeleteView,
    DetailView,
    CreateView,
    ListView,
    UpdateView,
) 

from queries.forms import ContactForm

def contact_us_view(request):
    contact_form = ContactForm(request.POST or None)
    if contact_form.is_valid():
        context['form'] = contact_form
        contact_form.save()
        
    context['form'] = contact_form
    return render(request, 'contact-us.htm', context=context)

class AboutUsView(TemplateView):
    template_name= 'about-us.htm'
    