from django.shortcuts import render

# Create your views here.
def TrabajosDisponibles(request):
    return render(request, 'base.html')