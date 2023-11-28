from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse

# Create your views here.
def home(request):    
    return render(request, 'home.html')

def registrarse(request):

    if request.method == 'GET':
        return render(request, 'registrarse.html',{
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(email=request.POST['email'], password=request.POST['password1'],roles=request.POST['roles'])
                user.save()
                return HttpResponse('Usuario Creado')
            except:
                return HttpResponse('Error en el formulario')
            
        return HttpResponse('Contraseñas no coinciden')


        

    

def ingresar(request):    
    return render(request, 'ingresar.html',{
        'form': UserCreationForm
    })
