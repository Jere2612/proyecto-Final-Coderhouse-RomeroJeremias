from django.shortcuts import render, redirect
from pre_entrega3.models import Alumno, Profesor , Institucion , Avatar
from django.http import HttpResponse
from django.template import loader
from pre_entrega3.forms import Alumno_formulario
from pre_entrega3.forms import Profesores_formulario
from pre_entrega3.forms import Institucion_formulario, UserEditForm
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required


def inicio(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    url_avatar = avatares[0].imagen.url if avatares else None
    if avatares:
        return render(request, 'inicio.html', {"url": url_avatar})
    else:
        return render(request, 'inicio.html')


def formulario_alumno(request):
    if request.method == "POST":
        mi_formulario = Alumno_formulario(request.POST) 
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            alumno = Alumno(nombre=datos['nombre'], comision=datos["comision"])
            alumno.save()
            return redirect('confirmacion')

    else:  
        mi_formulario = Alumno_formulario()
        avatares = Avatar.objects.filter(user=request.user.id)
        url_avatar = avatares[0].imagen.url if avatares else None
        if avatares:
            return render(request, "alumnos.html", {'form': mi_formulario, "url": url_avatar})
        else:
            return render(request, "alumnos.html", {'form': mi_formulario})



def confirmacion(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    url_avatar = avatares[0].imagen.url if avatares else None
    if avatares:
        return render(request, 'confirmacion.html', {"url": url_avatar})
    else:
        return render(request, 'confirmacion.html')


def formulario_profesor(request):
    if request.method == "POST":
        mi_formulario = Profesores_formulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            profesor = Profesor(nombre=datos['nombre'], legajo=datos["legajo"])
            profesor.save()
            return redirect('confirmacion')

    else: 
        mi_formulario = Profesores_formulario()
    
    avatares = Avatar.objects.filter(user=request.user.id)
    url_avatar = avatares[0].imagen.url if avatares else None
    if avatares:
        return render(request, "profesores.html", {'form': mi_formulario, "url": url_avatar}) 
    else:
        return render(request, "profesores.html")

def formulario_institucion(request):
    if request.method == "POST":
        mi_formulario = Institucion_formulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            institucion_instancia = Institucion(nombre=datos['nombre'],ciudad=datos['ciudad'], telefono=datos["telefono"])
            institucion_instancia.save()
            return redirect('confirmacion')

    else: 
        mi_formulario = Institucion_formulario()
    
    avatares = Avatar.objects.filter(user=request.user.id)
    url_avatar = avatares[0].imagen.url if avatares else None
    return render(request, "instituciones.html", {'form': mi_formulario, "url": url_avatar})


def ver_opciones(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    url_avatar = avatares[0].imagen.url if avatares else None
    return render(request, 'datos.html',{ "url": url_avatar})


def mostrar_datos_alumnos(request):
    avatares = Avatar.objects.all()  # Obtener todos los avatares, independientemente del usuario
    url_avatar = avatares[0].imagen.url if avatares else None
    alumnos = Alumno.objects.all()
    return render(request, 'read_alumnos.html', {'alumnos': alumnos, "url": url_avatar})

def mostrar_datos_profesores(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    url_avatar = avatares[0].imagen.url if avatares else None
    profesores = Profesor.objects.all()
    return render(request, 'read_profesores.html', {'profesores': profesores, "url": url_avatar})


def mostrar_datos_instituciones(request):
    instituciones = Institucion.objects.all()
    avatares = Avatar.objects.filter(user=request.user.id)
    url_avatar = avatares[0].imagen.url if avatares else None
    return render(request, 'read_instituciones.html', {'instituciones': instituciones,"url":url_avatar})




def buscar(request):
    if 'nombre' in request.GET:
        nombre = request.GET['nombre']
        alumnos = Alumno.objects.filter(nombre__icontains=nombre)
        avatares = Avatar.objects.filter(user=request.user.id)
        url_avatar = avatares[0].imagen.url if avatares else None
        if avatares:
            return render(request, "resultado_busqueda_alumnos.html", {"alumnos": alumnos, "url":url_avatar})
        else:
            return render(request, "resultado_busqueda_alumnos.html")
    else:
        return HttpResponse("Ingrese el nombre del alumno")



def busqueda_opciones(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    url_avatar = avatares[0].imagen.url if avatares else None
    return render(request, 'opciones_busqueda.html',{"url":url_avatar})


def buscar_profesores(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    url_avatar = avatares[0].imagen.url if avatares else None
    return render(request, 'busqueda_profesores.html',{"url":url_avatar})

def buscar_instituciones(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    url_avatar = avatares[0].imagen.url if avatares else None
    return render(request, 'busqueda_instituciones.html',{"url":url_avatar})


def buscar_alumnos(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    url_avatar = avatares[0].imagen.url if avatares else None
    return render(request, 'busqueda_alumnos.html',{"url":url_avatar})


def resultado_busqueda_alumnos(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    url_avatar = avatares[0].imagen.url if avatares else None
    nombre = request.GET.get('nombre')
    alumnos = Alumno.objects.filter(nombre__icontains=nombre)
    if avatares:
        return render(request, 'resultado_busqueda_alumno.html', {'alumnos': alumnos,"url":url_avatar})
    else:
        return render(request, 'resultado_busqueda_alumno.html')
def resultado_busqueda_profesores(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    url_avatar = avatares[0].imagen.url if avatares else None
    nombre = request.GET.get('nombre')
    profesores = Profesor.objects.filter(nombre__icontains=nombre)
    if avatares:
        return render(request, 'resultado_busqueda_profesores.html', {'profesores': profesores,"url":url_avatar})
    else:
        return render(request, 'resultado_busqueda_profesores.html')

def resultado_busqueda_instituciones(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    url_avatar = avatares[0].imagen.url if avatares else None
    nombre = request.GET.get('nombre')
    instituciones = Institucion.objects.filter(nombre__icontains=nombre)
    if avatares :
        return render(request, 'resultado_busqueda_instituciones.html', {'instituciones': instituciones,"url":url_avatar})
    else:
        return render(request, 'resultado_busqueda_instituciones.html')


def eliminar_alumno(request, id):
    avatares = Avatar.objects.filter(user=request.user.id)
    url_avatar = avatares[0].imagen.url if avatares else None
    alumno = Alumno.objects.get(id=id)
    alumno.delete()
    alumno = Alumno.objects.all()
    if avatares:
        return render(request , "read_alumnos.html" , {"alumnos":alumno,"url":url_avatar})
    else:
        return render(request , "read_alumnos.html" , {"alumnos":alumno})

def eliminar_profesor(request, id):
    avatares = Avatar.objects.filter(user=request.user.id)
    url_avatar = avatares[0].imagen.url if avatares else None
    profesor = Profesor.objects.get(id=id)
    profesor.delete()
    profesor = Profesor.objects.all()
    if avatares:
        return render(request , "read_profesores.html" , {"profesores":profesor, "url":url_avatar})
    else:
        render(request , "read_profesores.html" , {"profesores":profesor})
def eliminar_institucion(request, id):
    avatares = Avatar.objects.filter(user=request.user.id)
    url_avatar = avatares[0].imagen.url if avatares else None
    institucion = Institucion.objects.get(id=id)
    institucion.delete()
    institucion = Institucion.objects.all()
    if avatares:
        return render(request , "read_instituciones.html" , {"instituciones":institucion,"url":url_avatar})
    else:
        return render(request , "read_instituciones.html", {"instituciones":institucion})


def editar_alumno(request,id):
    avatares = Avatar.objects.filter(user=request.user.id)
    url_avatar = avatares[0].imagen.url if avatares else None
    alumno = Alumno.objects.get(id=id)
    if request.method == "POST":
        mi_formulario = Alumno_formulario( request.POST )
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            alumno.nombre = datos["nombre"]
            alumno.comision = datos["comision"]
            alumno.save()
            alumno = Alumno.objects.all()
            if avatares:
                return render(request , "read_alumnos.html" , {"alumnos":alumno, "url":url_avatar})
            else:
                return render(request , "read_alumnos.html" , {"alumnos":alumno})
    else:
        mi_formulario = Alumno_formulario(initial={"nombre":alumno.nombre , "comision":alumno.comision})
        if avatares:
            return render( request , "editar_alumno.html" , {"mi_formulario": mi_formulario , "alumno":alumno,"url":url_avatar})
        else:
            return render( request , "editar_alumno.html" , {"mi_formulario": mi_formulario , "alumno":alumno})

def editar_profesor(request,id):
    avatares = Avatar.objects.filter(user=request.user.id)
    url_avatar = avatares[0].imagen.url if avatares else None
    profesor = Profesor.objects.get(id=id)
    if request.method == "POST":
        mi_formulario = Profesores_formulario( request.POST )
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            profesor.nombre = datos["nombre"]
            profesor.legajo = datos["legajo"]
            profesor.save()
            profesor = Profesor.objects.all()
            if avatares:
                return render(request , "read_profesores.html" , {"profesores":profesor,"url":url_avatar})
            else:
                return render(request , "read_profesores.html" , {"profesores":profesor})
    else:
        mi_formulario = Profesores_formulario(initial={"nombre":profesor.nombre , "legajo":profesor.legajo})
        if avatares:
            return render( request , "editar_profesor.html" , {"mi_formulario": mi_formulario , "profesor":profesor, "url":url_avatar})
        else:
            return render( request , "editar_profesor.html" , {"mi_formulario": mi_formulario , "profesor":profesor})

def editar_institucion(request,id):
    avatares = Avatar.objects.filter(user=request.user.id)
    url_avatar = avatares[0].imagen.url if avatares else None
    institucion = Institucion.objects.get(id=id)
    if request.method == "POST":
        mi_formulario = Institucion_formulario( request.POST )
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            institucion.nombre = datos["nombre"]
            institucion.ciudad = datos["ciudad"]
            institucion.telefono = datos["telefono"]
            institucion.save()
            institucion = Institucion.objects.all()
            if avatares:
                return render(request , "read_instituciones.html" , {"instituciones":institucion,"url":url_avatar})
            else:
                return render(request , "read_instituciones.html" , {"instituciones":institucion})
    else:
        mi_formulario = Institucion_formulario(initial={"nombre":institucion.nombre , "ciudad":institucion.ciudad, "telefono":institucion.telefono})
        if avatares:
            return render( request , "editar_institucion.html" , {"mi_formulario": mi_formulario , "institucion":institucion, "url":url_avatar})
        else:
            return render( request , "editar_institucion.html" , {"mi_formulario": mi_formulario , "institucion":institucion})


def login_request(request):

    if request.method == "POST":
        if request.method == "POST":
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                usuario = form.cleaned_data.get("username")
                contra = form.cleaned_data.get("password")
                user = authenticate(username=usuario , password=contra)
                if user is not None:
                    login(request , user )
                    avatares = Avatar.objects.filter(user=request.user.id)
                    url_avatar = avatares[0].imagen.url if avatares else None
                    if avatares:
                        return render( request , "bienvenida.html" , {"url":url_avatar, "mensaje":f"Bienvenido/a {usuario}"})
                    else:
                        return render( request , "bienvenida.html" , {"mensaje":f"Bienvenido/a {usuario}"})
                else:
                    return HttpResponse(f"Usuario no encontrado")
            else:
                return HttpResponse(f"FORM INCORRECTO {form}")

    form = AuthenticationForm()
    return render( request , "login.html" , {"form":form})



def welcome(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    url_avatar = avatares[0].imagen.url if avatares else None
    if avatares:
        return render(request, "bienvenido.html",{"url":url_avatar})
    else:
        return render(request, "bienvenido.html")

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("bienvenido")
    else:
        avatares = Avatar.objects.filter(user=request.user.id)
        url_avatar = avatares[0].imagen.url if avatares else None
        form = UserCreationForm()
    if avatares:
        return render(request, "registro.html", {"form": form,"url":url_avatar})
    else:
        return render(request, "registro.html", {"form": form})



def editar_perfil(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    url_avatar = avatares[0].imagen.url if avatares else None
    usuario = request.user
    if request.method == "POST":
        mi_formulario = UserEditForm(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            usuario.email = informacion["email"]
            password = informacion["password1"]
            usuario.set_password(password)
            usuario.save()
            return render(request , "perfil_editado_confirmacion.html")
    else:
        mi_formulario = UserEditForm(initial={'email':usuario.email})
        if avatares:
            return render(request , "editar_perfil.html", {"miFormulario": mi_formulario, "usuario": usuario,"url":url_avatar})
        else:
            return render(request , "editar_perfil.html", {"miFormulario": mi_formulario, "usuario": usuario})
    
def editar_perfil_confirmacion(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    url_avatar = avatares[0].imagen.url if avatares else None
    if avatares:
        return render(request, 'perfil_editado_confirmacion.html',{"url":url_avatar})
    else:
        return render(request, 'perfil_editado_confirmacion.html')