from django.urls import path
from App.views import inicio, estudiantes, cursos, profesores, buscar, busqueda, formulario




urlpatterns = [
    path("inicio/", inicio, name="inicio"),
    path("estudiantes/", estudiantes, name="estudiantes") ,
    path("cursos/", cursos, name="cursos"),
    path("profesores/", profesores, name="profesores"),
    path("formulario/", formulario, name="formulario"),
    path("busqueda/", busqueda, name="busqueda"),
    path("buscar/", buscar, name="buscar"),
]    