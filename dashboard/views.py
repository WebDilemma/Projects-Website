from django.shortcuts import render, Http404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    TemplateView,
    DeleteView,
    DetailView,
    CreateView,
    ListView,
    UpdateView,
) 
from django.core.mail import mail_admins, send_mail
from django.conf import settings

from queries.forms import ContactForm

@login_required(login_url='profile:login')
def contact_us_view(request):
    context = {}
    contact_form = ContactForm(request.POST or None)
    if contact_form.is_valid():
        context['form'] = contact_form
        email = request.user.email
        print(request.user.email)
        instance = contact_form.save()
        instance.email = email
        
        instance.save()
        
        send_mail(
        instance.title,
        instance.text,
        settings.EMAIL_HOST_USER,
        ['parthishere1234@gmail.com'],
        fail_silently=False,
        )
        
        return redirect('contact_us_congo')
        
    context['form'] = contact_form
    return render(request, 'contact-us.htm', context=context)

class ContactUsResponse(TemplateView):
    template_name= 'contact-us-response.htm'

class AboutUsView(TemplateView):
    template_name= 'about-us.htm'
    