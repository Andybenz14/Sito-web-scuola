from django.urls import path
from . import views

urlpatterns = [
    path('', views.DocList.as_view(), name="modulistica"),
    path('search', views.SearchResult.as_view())
]

