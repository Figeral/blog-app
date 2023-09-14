from django.urls import path 
from . import  views

app_name="blog" #we named the app so a create a reference to it in the main url.py file of the project 
urlpatterns=[
    path('',views.post_list,name='post_list'),
    path('<int:id>',views.post_detail,name='post_detail'),
    path('published/',views.postpublish,name='postpublish'),
    path('<int:post_id>/share/',views.post_share,name='post_share')
]