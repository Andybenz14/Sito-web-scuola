from django.shortcuts import render

# Create your views here.


##CHI_SIAMO
def contatti(request):
    return render(request, "chi_siamo/contatti.html")

def orari(request):
    return render(request, "chi_siamo/orari.html")

def organigramma(request):
    return render(request, "chi_siamo/organigramma.html")


##SERVIZI
def iscrizione(request):
    return render(request, "servizi/iscrizione.html")

##PROGETTI
def cyberbullismo(request):
    return render(request, "progetti/cyberbullismo.html")

def PCTO(request):
    return render(request, "progetti/PCTO.html")

def PON(request):
    return render(request, "progetti/PON.html")

##PRIVACY
def privacy(request):
    return render(request, "privacy.html")
##DOVE siamo
def dove(request):
    return render(request, "dove.html")
