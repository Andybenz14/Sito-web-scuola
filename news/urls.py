from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name="notizie"),  #TODO: SEZIONE NOTIZIE!
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail')
]


