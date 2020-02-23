from django.urls import path
from . import views

urlpatterns = [
    path('', views.notizie, name="notizie")  #TODO: SEZIONE NOTIZIE!
]
