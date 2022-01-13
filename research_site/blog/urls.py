from django.urls import path, include

# Importing Views:
from .views import blog_index, blog_post

urlpatterns = [
    path("", blog_index, name="blog_home"), 
    path("posts/<str:topic>", blog_index, name="blog_category"),
    path("post/<str:slug>", blog_post, name="blog_post")

]