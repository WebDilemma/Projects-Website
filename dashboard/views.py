from django.shortcuts import render, Http404, redirect, HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    TemplateView,
    DeleteView,
    DetailView,
    CreateView,
    ListView,
    UpdateView,
) 
from django.core.mail import mail_admins, send_mail, BadHeaderError
from django.conf import settings
from django.template.loader import render_to_string, get_template

from queries.forms import ContactForm


def contact_us_view(request):
    context = {}
    contact_form = ContactForm(request.POST or None)
    if contact_form.is_valid():
        context['form'] = contact_form
        
        instance = contact_form.save()
        context = {
            'superuser': "parth",
            'title': instance.title,
            'message': instance.text,
            'email': instance.email,
        }
        
        subject = instance.title
        message = render_to_string('email.html', context) 
        from_email = instance.email
    
        try:
            mail_admins(subject, message, fail_silently=False, html_message=message)
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return redirect('contact_us_congo')
        
    context['form'] = contact_form
    return render(request, 'contact-us.htm', context=context)

class ContactUsResponse(TemplateView):
    template_name= 'contact-us-response.htm'

class AboutUsView(TemplateView):
    template_name= 'about-us.htm'
    