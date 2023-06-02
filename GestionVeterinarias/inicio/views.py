from django.shortcuts import render


# Create your views here.

#pagina de inicio
def home(request):
    return render(request,"inicio/home.html")
