from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .models import Residente,departamento,Gasto_Comun
from .forms import UsuarioForm,UpdUsuarioForm,DepartamentoForm,GastoComunForm,UpDepaForm,UpGastoForm

#funciones para residentes
def index(request):
    residente = Residente.objects.all()
    print(residente)
    datos={
        'user':residente
    }
    print(datos)
    return render(request,'aplicacion/index.html',datos)

#Vista para actualizar residente
def update(request,id):
    residente=get_object_or_404(Residente,rut=id)
    formU=UpdUsuarioForm(instance=residente)
    if request.method=='POST':
        formU=UpdUsuarioForm(request.POST,files=request.FILES, instance=residente)
        if formU.is_valid():
            formU.save()
            messages.set_level(request,messages.WARNING)
            messages.warning(request,"Residente Modificado")
            return redirect('index')
    datos={
        'formU':formU,
        'usuario':residente
    }
    return render(request,'aplicacion/actualizar.html',datos)

#vista para ingresar residente
def ingresar(request):
    if request.method == 'POST':
        formulario = UsuarioForm(request.POST, files=request.FILES)  
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Residente agregado exitosamente")
            return redirect('index')
        else:
            messages.error(request, "Error al agregar el Residente")
            return redirect('index')
    else:
        formulario = UsuarioForm()  

    datos = {
        'form': formulario,
    }
    return render(request, 'aplicacion/ingresar.html', datos)

#vista para eliminar residente
def eliminar(request, id):
    usuario = get_object_or_404(Residente, rut=id)  
    usuario.delete()  
    return redirect('index')

#Funciones para departamento
def depart(request):
    depa=departamento.objects.all()
    print(depa)
    datos={
        'depa':depa
    }
    return render(request,'aplicacion/departamentos.html',datos)
#agregar el departamento
def ingresardepto (request):
    if request.method == 'POST':
        formulario = DepartamentoForm(request.POST, files=request.FILES)  
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Informacion del Departamento agregado exitosamente")
            return redirect('departamentos')
        else:
            messages.error(request, "Error al agregar la informacion del Departamento")
            return redirect('departamentos')
    else:
        formulario = DepartamentoForm()

    datos = {
        'formulario': formulario,
    }
    return render(request,'aplicacion/ingresardepto.html',datos)
#actualizar departamento
def updepa (request,id):
    depa=get_object_or_404(departamento,numero_piso=id)
    formU=UpDepaForm(instance=depa)
    if request.method=='POST':
        formU=UpDepaForm(request.POST,files=request.FILES, instance=depa)
        if formU.is_valid():
            formU.save()
            messages.set_level(request,messages.WARNING)
            messages.warning(request,"Residente Modificado")
            return redirect('departamentos')
    datos={
        'formU':formU,
        'usuario':depa
    }
    return render(request,'aplicacion/updepa.html',datos)

#eliminar departamento
def eliminardepa(request,id):
    depa = get_object_or_404(departamento, numero_piso=id)  
    depa.delete()  
    return redirect('departamentos')

#funciones para gastos comunes
def gastos (request):
    gastos=Gasto_Comun.objects.all()
    datos={
        "gasto":gastos
    }
    return render (request,'aplicacion/gastos.html',datos)

#agregar gastos
def agregargasto(request):
    if request.method == 'POST':
        formulario = GastoComunForm(request.POST, files=request.FILES)  
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Gasto agregado exitosamente")
            return redirect('index')
        else:
            messages.error(request, "Error al agregar la Gasto")
            return redirect('Gastos')
    else:
        formulario = GastoComunForm()

    datos = {
        'formulario': formulario,
    }
    return render (request,'aplicacion/ingresargasto.html',datos)

#actualizar el gasto
def UpGasto(request, id):
    gasto = get_object_or_404(Gasto_Comun, id_gasto_comun=id)
    if request.method == 'POST':
        formU = UpGastoForm(request.POST, files=request.FILES, instance=gasto)
        if formU.is_valid():
            formU.save()
            messages.warning(request, "Gasto actualizado correctamente.")
            return redirect('departamentos')
    else:
        formU = UpGastoForm(instance=gasto)

    datos = {
        'formU': formU,
        'usuario': gasto
    }
    return render(request, 'aplicacion/Upgasto.html', datos)

#eliminar gasto
def eliminarGasto(request,id):
    gasto = get_object_or_404(Gasto_Comun, id_gasto_comun=id)  
    gasto.delete()  
    return redirect('Gastos')
