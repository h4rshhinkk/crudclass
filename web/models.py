from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class Core(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(null=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE, related_name='core')
    slug = models.SlugField(max_length=200, unique=True)
    updated = models.DateTimeField(auto_now=True)
    published  = models.DateTimeField(default=timezone.now)


    def get_absolute_url(self):
        return reverse('web:single', args=[self.slug])
    
    class Meta:
        ordering = ['-published']

    
    def __str__(self):
        return str(self.title)