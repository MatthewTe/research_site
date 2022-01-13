from django.contrib import admin

# Importing Blog models:
from .models import BlogPost

admin.site.register(BlogPost)