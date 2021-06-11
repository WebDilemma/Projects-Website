from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse

from portfolio.models import UserProfile

from rest_framework.reverse import reverse as api_reverse

# Create your models here.
class OurTeam(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=100, null=True, blank=True)
    job_title = models.CharField(max_length=100, null=True, blank=True)
    expertise = models.CharField(max_length=100, null=True, blank=True)

    
    
    def __str__(self):
        return self.user.user.username
    
    def get_absolute_url(self):
        return reverse("team:detail", kwargs={"slug": self.user.slug})
    
    def get_api_url(self, request=None):
        return api_reverse('team-api:detail-api', kwargs={"pk": self.pk}, request=request)
    
    # reverse queryset when user = User not UserProfile
    # def get_absolute_url(self):
    #     return reverse("team:detail", kwargs={"slug": self.user.user_profile.slug})
    
    
    