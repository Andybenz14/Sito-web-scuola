"""sito URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from . import views

from news.views import IndexPostList# This is horrible

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', IndexPostList.as_view(), name="index"),
    path('notizie/', include("news.urls")),  # TODO: SEZIONE NOTIZIE!

    ##CHI SIAMO
    path('contatti/', views.contatti, name="contatti"),
    path('orari/', views.orari, name="orari"),
    path("organigramma/", views.organigramma, name="organigramma"),

    ##SERVIZI
    path('iscrizione/', views.iscrizione, name="iscrizione"),
    path('scuolainchiaro/', views.scuolainchiaro, name="scuolainchiaro"),
    ##PROGETTI
    path('cyberbullismo/', views.cyberbullismo, name="cyberbullismo"),
    path('PON/', views.PON, name="PON"),
    path('PCTO/', views.PCTO, name="PCTO"),

    ##PRIVACY
    path('privacy/', views.privacy, name="privacy"),

    ##DOVE SIAMO
    path('dove/', views.dove, name="dove"),

    ##ACCESSO
    path('accesso/', views.accesso, name="accesso"),
]





# Import settings if not imported
from django.conf import settings
# Import static if not imported
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
