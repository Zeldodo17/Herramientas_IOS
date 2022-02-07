from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from .models import (
    Herramientas,
    Usuario,
    Videos
)
from .forms import (
    FormLogin,
    FormRegister
)


# Create your views here.

@login_required
def Inicio(request):
    # guardamos lo que se introdujo en los campos de busqueda
    busqueda = request.POST.get("buscar")
    busquedaCurso = request.POST.get("buscarVideo")
    herramientas = None
    videos = None
    # Si el usuario busco gerramientas entra a este if
    if busqueda:
        # Filtramos las herramientas con respecto a lo que tiene busqueda
        herramientas = Herramientas.objects.filter(
            Q(nombre__icontains=busqueda) |
            Q(clasificacion__nombre__icontains=busqueda)
        ).distinct()
        # Si busco un curso entra a este elif 
    elif busquedaCurso:
        # Filtramos las herramientas con respecto a lo que tiene busquedaCurso
        videos = Videos.objects.filter(
            Q(nombre__icontains=busquedaCurso) |
            Q(unidad__nombre__icontains=busquedaCurso)
        )
    else:
        # Si no se esta busando 1 herramienta o curso especifico, se devuelven todos los cursos  y las herramientas
        videos = Videos.objects.all()
        herramientas = Herramientas.objects.all()
        # Creamos un diccionario donde ponemos lo que vamos a mandar al template
    data = {
        'Herramientas': herramientas,
        'Videos': videos,
        'Texto': 'Textito'
    }
    # Usamos el metodo render para renderizar los datos que estan dentro del diccionario data en la plantilla index.html
    return render(request, 'index.html', data)

def crearUsuario(request):
    if request.method == 'POST':
        formulario = FormRegister(request.POST, files=request.FILES)
        if formulario.is_valid():
            data_form = formulario.cleaned_data

            nombres = data_form.get('nombres')
            username = data_form.get('username')
            correo = data_form.get('email')
            imagen = data_form.get('imagen')
            password = make_password(data_form.get('password'))

            crearusuario = Usuario(
                nombres=nombres,
                username=username,
                email=correo,
                imagen=imagen,
                password=password,
            )
            crearusuario.save()
            return redirect(to='login')
    else:
        formulario = FormRegister()
    return render(request, 'registration/login.html', {
        'form': formulario
    })
