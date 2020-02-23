from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('notizie/', views.index, name="notizie"), #TODO: SEZIONE NOTIZIE!

    ##CHI SIAMO
    path('contatti/', views.contatti, name="contatti"),
    path('orari/', views.orari, name="orari"),
    path("organigramma/", views.organigramma, name="organigramma"),

    ##SERVIZI
    path('iscrizione/', views.iscrizione, name="iscrizione"),

    ##PROGETTI
    path('cyberbullismo/', views.cyberbullismo, name="cyberbullismo"),
    path('PON/', views.PON, name="PON"),
    path('PCTO/', views.PCTO, name="PCTO"),

    ##PRIVACY
    path('Privacy/', views.Privacy, name="Privacy"),

    ##DOVE SIAMO
    path('dove/', views.dove, name="dove"),

]
