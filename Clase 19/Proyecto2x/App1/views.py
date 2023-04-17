from django.shortcuts import render
from App1.models import Curso
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