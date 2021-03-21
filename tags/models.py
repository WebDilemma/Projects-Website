from django.db import models

from django.shortcuts import reverse, render

# Create your models here.
class Tag(models.Model):
    tag = models.CharField(max_length=50)
    
    class Meta():
        ordering = ['-id']
        
    def __str__(self):
        return self.tag
    
