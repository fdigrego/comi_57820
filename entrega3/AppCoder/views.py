from django.shortcuts import render, redirect
from django.http import HttpResponse
from AppCoder.models import Curso, Profesor, Estudiante, Entregable
from AppCoder.forms import CursoFormulario

# Create your views here.

def inicio(request):
    return render(request, "AppCoder/index.html")
def cursos(request):
    return render(request, "AppCoder/cursos.html")
def profesores(request):
    return render(request, "AppCoder/profesores.html")
def estudiantes(request):
    return render(request, "AppCoder/estudiantes.html")
def entregables(request):
    return render(request, "AppCoder/entregables.html")

def cursoFormulario(request):
    
    if request.method == "POST":
        miFormulario = CursoFormulario(request.POST)
        print(miFormulario)
        
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            curso = Curso(nombre=informacion['curso'], camada=informacion['camada'])
            curso.save()
            return render(request, "AppCoder/cursoFormulario.html", {"miFormulario": miFormulario})
            #return redirect('cursos')

    else:
        miFormulario = CursoFormulario()

    return render(request, "AppCoder/cursoFormulario.html", {"miFormulario": miFormulario})

def estudianteFormulario(request):
    return render(request, "AppCoder/estudianteFormulario.html")
def profesorFormulario(request):
    return render(request, "AppCoder/profesorFormulario.html")
def entregableFormulario(request):
    return render(request, "AppCoder/entregableFormulario.html")
