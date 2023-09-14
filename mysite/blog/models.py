from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class publishedmanager(models.Manager): # custom manager creation 
    def get_queryset(self):
        return super(publishedmanager,self).get_queryset()\
                                           .filter(status="published")

class post(models.Model):
    STATUS_CHOICES = (
     ('draft', 'Draft'),
     ('published', 'Published'),
    ) 
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,unique_for_date='publish')
    author=models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='blog_posts')
    # profile = models.ImageField()
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                                choices=STATUS_CHOICES,
                                default='draft')
    objects=models.Manager() #default manager 
    Published=publishedmanager() # custom manager 
    class meta:
        ordering=('-publish',)
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.id]
                       )
        