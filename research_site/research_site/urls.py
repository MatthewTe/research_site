# Stock Django methods:
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # Default Routes:
    path('admin/', admin.site.urls),
    
    path("", include("research_core.urls")),
    path("blog/", include("blog.urls")),

    # Third Party Routes:
    path("tinymce/", include("tinymce.urls"))
]

# Adding development url for uploading and accessing images:
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)