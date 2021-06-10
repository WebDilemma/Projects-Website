from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class OurTeam(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=100, null=True, blank=True)
    job_title = models.CharField()(max_length=100, null=True, blank=True)
    expertise = models.CharField(max_length=100, null=True, blank=True)
    profile_pic = models.ImageField(upload_to='team/profile', null=True, blank=True)
    github_link = models.URLField(blank=True, null=True)
    website_link = models.URLField(blank=True, null=True)
    twitter_handle = models.URLField(blank=True, null=True)
    linked_in_link = models.URLField(blank=True, null=True)
    instagram_profile_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.user.username
    
    