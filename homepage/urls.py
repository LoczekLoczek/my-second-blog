from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('kontakt.html', views.home1, name="home1"),
    path('mapa.html', views.home2, name="home2"),
    path('naszemarki.html', views.home3, name="home3"),
]