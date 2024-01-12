from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from .views import login_view, logout_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/", include("recipes.urls")),
    path("", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("profile/", include("profiles.urls")),
    path("add_recipe/", include("recipes.urls")),
    path("about/", include("profiles.urls")),
]

# Corrected pattern for serving media files during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
