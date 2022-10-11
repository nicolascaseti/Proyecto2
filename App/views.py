from django.shortcuts import render
from App.models import Estudiante, Profesor, Curso 
from App.forms import cursoFormulario
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    return render(request, "App/inicio.html")

def cursos(request):
    return render(request, "App/cursos.html")

def profesores(request):
    return render(request, "App/profesores.html")

def estudiantes(request):
    return render(request, "App/estudiantes.html")

def formulario(request):
    
    if request.method != "POST":
        mi_formulario = cursoFormulario()
    else:
        mi_formulario = cursoFormulario(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            curso = Curso(nombre=informacion["curso"], comision=informacion["comision"])
            curso.save()
            return render(request, "App/inicio.html")
    
    contexto = {"formulario": mi_formulario}
    
    return render(request, "App/formulario.html", contexto)

def busqueda(request):
    return render(request, "App/busqueda.html")

def buscar(request):
    if not request.GET["comision"]:
        return HttpResponse("Reintente Nuevamente")
    else:
        comision_buscada = request.GET["comision"]
        cursos = Curso.objects.filter(comision=comision_buscada)
    
        contexto = {
            "comision": comision_buscada,
            "cursos_encontrados": cursos
        }
        return render(request, "App/resultado_busqueda.html", contexto)

