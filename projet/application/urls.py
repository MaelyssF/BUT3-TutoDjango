from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home1"),
    path("home", views.home, name="home2"),
    path("home/<param>", views.home_param, name="home_param"),
    path("contact", views.contact, name="contact"),
    path("about", views.about, name="about")
] 