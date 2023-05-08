from django.urls import path
from App1 import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('',views.inicio, name="Inicio"), #este era nuestro primer view
    path('cursos', login_required(views.cursos), name="Cursos"),
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
    path(r'^borrar/(?P<pk>\d+)$',views.CursoDelete.as_view(),name='Delete'),
    path('login/',views.login_request, name="Login"),
    path('register/', views.register, name='Register'),
    path('logout', LogoutView.as_view(template_name='App1/logout.html'), name='Logout'),
    path("my-page/", views.MyView.as_view(), name="my_page"),
    path("my-protected-page/", views.MyProtectedView.as_view(), name="my_protected_page"),
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"), 
    path('agregarAvatar', views.agregarAvatar, name="AgregarAvatar"), 
]
