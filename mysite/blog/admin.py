from django.contrib import admin
from .models import post

@admin.register(post)
class postAdmin(admin.ModelAdmin):
    list_display=['title','slug','author','publish','status']
    search_fields=['title','status']
    prepopulated_fields={'slug':('title',)}
    raw_id_fields=['author']
    date_hierarchy='publish'
    
