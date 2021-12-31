# Native Django Imports:
from django.urls import path, include

# Importing core site views:
from .views import site_index

urlpatterns = [
    path("", site_index, name="site_index")
]