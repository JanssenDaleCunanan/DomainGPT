from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("DomainSearch/", views.DomainSearch, name="DomainSearch"),
    path("suggestions/",views.suggestions, name="suggestions"),
    path("availability/",views.availability, name="availability"),
]