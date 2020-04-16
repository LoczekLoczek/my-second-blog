from django.shortcuts import render




def home(request):
    return render(request, 'Zanurzone.html')

def home1(request):
    return render(request, 'kontakt.html')

def home2(request):
    return render(request, 'mapa.html')

def home3(request):
    return render(request, 'naszemarki.html')

def home4(request):
    return render(request, 'politykaprywatnosci.html')