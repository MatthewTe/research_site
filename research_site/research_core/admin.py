# Importing stock django methods:
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Importing User Model:
from .models import CustomUser

# Importing Research Models:
from .models import Organization, Topic, Publication, Author, Source 

# Registering the Custom User Model to the admin dash:
admin.site.register(CustomUser, UserAdmin)

# Adding all of the Research models to the admin dashboard:
admin.site.register(Source)
admin.site.register(Author)
admin.site.register(Publication)
admin.site.register(Topic)
admin.site.register(Organization)