from django.shortcuts import render

# Create your views here.

def notizie(request):
    return render(request, "notizie.html")