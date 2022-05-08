from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.home, name = 'home'),
    path("home", views.home, name = 'home'),
    path("about", views.about, name = 'about'),
    path("write", views.write, name = 'write'),
    path("contact", views.contact, name = 'contact')
]