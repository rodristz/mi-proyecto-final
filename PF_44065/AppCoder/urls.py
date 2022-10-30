from django.urls import path
from PF_44065.AppCoder import views





urlpatterns = [
   
    path('', views.inicio, name="Inicio"), #esta era nuestra primer view
    path('cursos', views.cursos, name="Cursos"),
    path('profesores', views.profesores, name="Profesores"),
    path('estudiantes', views.estudiantes, name="Estudiantes"),
    path('entregables', views.entregables, name="Entregables"),
    path('cursoFormulario', views.CursoFormulario, name="CursoFormulario"),
    path('profesorFormulario', views.ProfesorFormulario, name="ProfesorFormulario"),
    # path('busquedaCamada',  views.BusquedaCamada, name="BusquedaCamada"),
    path('buscar/', views.buscar),
   
]

