from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from aplicacion.models import Usuario
from .forms import UsuarioForm,UpdUsuarioForm

# Create your views here.
def index(request):
    usuario = Usuario.objects.all()
    print(usuario)
    datos={
        'user':usuario
    }
    print(datos)
    return render(request,'aplicacion/index.html',datos)

def update(request,id):
    usuario=get_object_or_404(Usuario,rut=id)
    formU=UpdUsuarioForm(instance=usuario)
    if request.method=='POST':
        formU=UpdUsuarioForm(request.POST,files=request.FILES, instance=usuario)
        if formU.is_valid():
            formU.save()
            messages.set_level(request,messages.WARNING)
            messages.warning(request,"Usuario Modificado")
            return redirect('index')
    datos={
        'formU':formU,
        'usuario':usuario
    }
    return render(request,'aplicacion/actualizar.html',datos)
def ingresar(request):
    if request.method == 'POST':
        formulario = UsuarioForm(request.POST, files=request.FILES)  # Corregido 'files'
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto agregado exitosamente")
            return redirect('index')
        else:
            messages.error(request, "Error al agregar el producto")
            return redirect('index')
    else:
        formulario = UsuarioForm()  # Definir formulario también para solicitudes GET

    # Pasar formulario al contexto para que se muestre en la plantilla
    datos = {
        'form': formulario,
    }
    return render(request, 'aplicacion/ingresar.html', datos)

def eliminar(request, id):
    usuario = get_object_or_404(Usuario, rut=id)  
    usuario.delete()  
    return redirect('index')