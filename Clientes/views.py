from django.shortcuts import render

# Create your views here.
def PublicarProblema(request):
    return render(request, 'PublicarProblema.html')