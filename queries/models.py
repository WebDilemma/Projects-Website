from django.db import models
from django.db.models.signals import pre_save, post_save
# Create your models here.
class ContactModel(models.Model):
    email = models.EmailField()
    title = models.CharField(max_length=100)
    text = models.TextField()
    
    class Meta():
        ordering = [ '-id' ]
        
    def __str__(self):
        return self.email
    

