from django.urls import path
from .views import profile_view, about_me_view

app_name = "profiles"

urlpatterns = [
    path("", profile_view, name="profile"),
    path("about/", about_me_view, name="about-me"),
]
