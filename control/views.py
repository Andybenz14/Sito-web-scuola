from django.shortcuts import render

# Create your views here.


##Informazioni
def chisiamo(request):
    return render(request, "Informazioni/chisiamo.html")

def contatti(request):
    return render(request, "Informazioni/contatti.html")

def orari(request):
    return render(request, "Informazioni/orari.html")

def organigramma(request):
    return render(request, "Informazioni/organigramma.html")


##SERVIZI
def iscrizione(request):
    return render(request, "servizi/iscrizione.html")
def scuolainchiaro(request):
    return render(request, "servizi/scuolainchiaro.html")
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
##DOVE SIAMO
def dove(request):
    return render(request, "dove.html")
##ACCESSO
def accesso(request):
    return render(request, "accesso.html")
##LINK ISTITUZIONALI
def albo(request):
    return render(request, "albo.html")
##MODULISTICA
def modulistica(request):
    return render(request, "modulistica.html")
