from django.urls import path
from App1 import views
urlpatterns = [
    path('', views.inicio, name="Inicio"), #este era nuestro primer view
    path('cursos', views.cursos, name="Cursos"),
    path('profesores', views.profesores, name="Profesores"),
    path('estudiantes', views.estudiantes, name="Estudiantes"),
    path('entregables', views.entregables, name="Entregables"),
    #path('cursoFormulario', views.cursoFormulario, name="CursoFormulario"),
    #path('profesorFormulario', views.profesorFormulario, name="ProfesorFormulario"),
    #path('busquedaCurso',views.busquedaCurso,name="BusquedaCurso"),
    path('buscar/',views.buscar),
    path('leerProfesores',views.leerProfesores,name='LeerProfesores'),
    path('eliminarProfesor/<profesor_nombre>/', views.eliminarProfesor, name="EliminarProfesor"),
    path('editarProfesor/<profesor_nombre>/', views.editarProfesor, name="EditarProfesor"),
    path('curso/list',views.CursoList.as_view(),name='List'),
    path(r'^(?P<pk>\d+)$', views.CursoDetalle.as_view(),name='Detail'),
    path(r'^nuevo$', views.CursoCreacion.as_view(),name='New'),
    path(r'^editar/(?P<pk>\d+)$',views.CursoUpdate.as_view(),name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$',views.CursoDelete.as_view(),name='Delete')

]
