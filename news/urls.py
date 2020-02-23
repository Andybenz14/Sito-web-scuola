from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('notizie/', views.index, name="notizie"), #TODO: SEZIONE NOTIZIE!
]
