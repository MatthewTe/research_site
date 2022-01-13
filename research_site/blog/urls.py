from django.urls import path, include

# Importing Views:
from .views import blog_index, blog_post

urlpatterns = [
    path("", blog_index, name="blog_home"),
    path("<str:slug>", blog_post, name="blog_post")

]