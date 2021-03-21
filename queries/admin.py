from django.contrib import admin

# Register your models here.
from .models import ContactModel

admin.site.register(ContactModel)