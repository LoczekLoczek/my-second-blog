from django.shortcuts import render




def home(request):
    return render(request, 'Zanurzone.html')

def home1(request):
    return render(request, 'kontakt.html')