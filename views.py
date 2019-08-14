from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'rai_app/index.html')
def pestana(request):
    return render(request, 'rai_app/pestana.html')
def desafio2(request):
    return render(request, 'rai_app/desafio2.html')

