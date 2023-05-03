from django.shortcuts import render
from App1.models import Curso, Profesor
from App1.forms import CursoFormulario, ProfesorFormulario
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def inicio(request):
    return render(request, 'App1/inicio.html')
@login_required
def cursos(request):
    return render(request,'App1/cursos.html')
def profesores(request):
    return render(request,'App1/profesores.html')
def estudiantes(request):
    return render(request,'App1/estudiantes.html')
def entregables(request):
    return render(request,'App1/entregables.html')
def cursoFormulario(request):
      if request.method == 'POST':
            curso =  Curso(request.post['nombre'],(request.post['curso']))
            curso.save()
            return render(request, "App1/inicio.html")
      return render(request,"App1/cursoFormulario.html")

'''
def cursoFormulario(request):
      if request.method == "POST":
            miFormulario = CursoFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)

            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  curso = Curso(int(informacion['id']),str(informacion['nombre']),int(informacion['curso']))
                  curso.save()
                  return render(request, "App1/inicio.html")
      else:
            miFormulario = CursoFormulario()
 
      return render(request, "App1/cursoFormulario.html", {"miFormulario": miFormulario})
'''

def cursos(request):
    if request.method =='POST':
        miFormulario=CursoFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion=miFormulario.cleaned_data
            curso=Curso(int(informacion['id']),str(informacion['nombre']),int(informacion['curso']))
            curso.save()
            return render(request, 'App1/inicio.html')
    else:
        miFormulario=CursoFormulario()
    return render(request, 'App1/cursos.html', {"miFormulario": miFormulario})

def profesorFormulario(request):
     if request.method == "POST":
        miFormulario = ProfesorFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            curso = Profesor(int(informacion['id']),str(informacion['nombre']),str(informacion['apellido']),
                                   informacion['email'], informacion['profesion'])
            curso.save()
            return render(request, "App1/inicio.html")
     else:
        miFormulario = ProfesorFormulario()
             
     return render(request, "App1/profesorFormulario.html", {"miFormulario": miFormulario})

def busquedaCurso(request):
     return render(request,'App1/busquedaCurso.html')

#def buscar(request):
#     respuesta= f"Estoy buscando la comision nro: {request.GET['curso']}"
#     return HttpResponse(respuesta)

def buscar(request):
     if request.GET['curso']:
          curso = request.GET['curso']
          cursos= Curso.objects.filter(curso__icontains=curso)

          return render(request,'App1/inicio.html', {"cursos":cursos, "comisiones": curso })
     else:
          respuesta= "No enviaste datos"

     #return HttpResponse(respuesta)
     return render(request,"App1/inicio.html",{"respuesta":respuesta})

def leerProfesores(request):
    profesores= Profesor.objects.all() # trae a todos los profesores
    contexto= {"profesores": profesores}
    return render(request, "App1/leerProfesores.html",contexto)

def eliminarProfesor(request, profesor_nombre):
    profesor = Profesor.objects.get(nombre=profesor_nombre)
    profesor.delete()
    # vuelvo al menú
    profesores = Profesor.objects.all()  # trae todos los profesores 
    contexto = {"profesores": profesores}
    return render(request, "App1/leerProfesores.html", contexto)

def editarProfesor(request, profesor_nombre):
    # Recibe el nombre del profesor que vamos a modificar
    profesor = Profesor.objects.get(nombre=profesor_nombre)
    # Si es metodo POST hago lo mismo que el agregar
    if request.method == 'POST':
        # aquí mellega toda la información del html
        miFormulario = ProfesorFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:  # Si pasó la validación de Django
            informacion = miFormulario.cleaned_data

            profesor.nombre = informacion['nombre']
            profesor.apellido = informacion['apellido']
            profesor.email = informacion['email']
            profesor.profesion = informacion['profesion']
            profesor.save()

            # Vuelvo al inicio o a donde quieran
            return render(request, "App1/inicio.html")
    # En caso que no sea post
    else:
        # Creo el formulario con los datos que voy a modificar
        miFormulario = ProfesorFormulario(initial={'nombre': profesor.nombre, 'apellido': profesor.apellido,
                                                   'email': profesor.email, 'profesion': profesor.profesion})
    # Voy al html que me permite editar
    return render(request, "App1/editarProfesor.html", {"miFormulario": miFormulario, "profesor_nombre": profesor_nombre})

from django.views.generic import ListView
class CursoList(ListView):
    model =Curso 
    template_name='/App1/curso_list.html'

from django.views.generic.detail import DetailView
class CursoDetalle(DetailView):
    model=Curso 
    template_name= "App1/curso_detalle.html"

from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
class CursoCreacion(CreateView):
    model=Curso
    success_url="/App1/curso/list"
    fields= ['nombre','curso']

from django.views.generic.edit import UpdateView
class CursoUpdate(UpdateView):
    model=Curso
    success_url= "/App1/curso/list"
    fields=['nombre','curso']

from django.views.generic.edit import DeleteView
class CursoDelete(DeleteView):
    model=Curso
    success_url="/App1/curso/list"

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():  # Si pasó la validación de Django
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')
            user = authenticate(username= usuario, password=contrasenia)
            if user is not None:
                login(request, user)
                return render(request, "App1/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "App1/inicio.html", {"mensaje":"Datos incorrectos"})
        else:
            return render(request, "App1/inicio.html", {"mensaje":"Formulario erroneo"})
    form = AuthenticationForm()
    return render(request, "App1/login.html", {"form": form})


from App1.forms import UserRegisterForm
@login_required
def register(request):
      if request.method == 'POST':
            #form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"App1/inicio.html" ,  {"mensaje":"Usuario Creado :)"})
      else:
            #form = UserCreationForm()       
            form = UserRegisterForm()     
      return render(request,"App1/registro.html" ,  {"form":form})