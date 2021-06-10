from django.db import models
from django.shortcuts import redirect, reverse
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save

from rest_framework.reverse import reverse as api_reverse

import portfolio
import tags
from .utils import random_string_generator

CATEGORIE_CHOICES = [
    ('BG', 'BLOG'),
    ('EN', 'ENTERTAINMENT'),
    ('EC', 'ECOMMERCE'),
    ('TC', 'TECH'),
    ('O', 'OTHER')
]

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=50)
    img = models.ImageField(upload_to='projects/')
    author = models.ManyToManyField('portfolio.UserProfile', related_name='project_user')
    text = models.TextField()
    slug = models.SlugField(blank=True, null=True)
    like = models.ManyToManyField(portfolio.models.UserProfile,related_name='like', blank=True)
    categorie = models.CharField(choices=CATEGORIE_CHOICES, max_length=2)
    link = models.URLField(verbose_name="link_to_project", name='link')
    # tools = models.ManyToManyField('tags.Tag', related_name='tools')
    
    class Meta():
        ordering = [ '-id' ]
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("projects:detail", kwargs={"slug": self.slug})
    
    def get_api_url(self, request=None):
        return api_reverse('project-api:detail-api', kwargs={"slug": self.slug}, request=request)
    
    @property
    def owner(self):
        return self.author
    
def unique_slug_generator_project(instance, new_slug=None):
    """
    This is for a Django project and it assumes your instance
    has a model with a slug field and a title character (char) field.
    """
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
                    slug=slug,
                    randstr=random_string_generator(size=4)
                )
        return unique_slug_generator_project(instance, new_slug=new_slug)
    return slug


def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator_project(instance)
pre_save.connect(product_pre_save_receiver, sender=Project)


