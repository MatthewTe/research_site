# Native Django Imports:
from django.urls import path, include

# Importing core site views:
from .views import site_index, research_main_page, research_topic

urlpatterns = [
    path("", site_index, name="site_index"),
    path("research", research_main_page, name="research_home"),
    path("research/<str:topic>", research_topic, name="research_topic")
]