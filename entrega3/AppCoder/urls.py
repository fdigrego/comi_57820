from django.urls import path
from AppCoder import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('cursos/', views.cursos, name='cursos'),
    path('profesores/', views.profesores, name='profesores'),
    path('estudiantes/', views.estudiantes, name='estudiantes'),
    path('entregables/', views.entregables, name='entregables'),
    
    path('cursoFormulario/', views.cursoFormulario, name='cursoFormulario'),
    path('estudianteFormulario/', views.estudianteFormulario, name='estudianteFormulario'),
    path('profesorFormulario/', views.profesorFormulario, name='profesorFormulario'),
    path('entregableFormulario/', views.entregableFormulario, name='entregableFormulario'),
    
    #path('busquedaComision', views.busquedaComision, name='busquedaComision'),
    #path('buscar', views.buscar),
]
