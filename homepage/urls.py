from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('kontakt.html', views.home1, name="home1"),
]