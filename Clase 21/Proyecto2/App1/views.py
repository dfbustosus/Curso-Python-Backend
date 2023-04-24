from django.shortcuts import render
from App1.models import Curso, Profesor
from App1.forms import CursoFormulario, ProfesorFormulario
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return render(request, 'App1/inicio.html')
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

