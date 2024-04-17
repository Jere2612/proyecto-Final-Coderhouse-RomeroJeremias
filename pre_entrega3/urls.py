from django.urls import path
from pre_entrega3 import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',views.inicio, name='home' ),
    path('alta_alumnos',views.formulario_alumno, name='alumnos'),
    path('instituciones', views.formulario_institucion,name='instituciones'),
    path('profesores', views.formulario_profesor, name='profesores'),
    path('ver_datos', views.ver_opciones, name='ver_datos'),
    path('read_alumnos',views.mostrar_datos_alumnos, name='ver_alumnos'),
    path('confirmacion',views.confirmacion, name='confirmacion'),
    path('ver_datos/read_profesores', views.mostrar_datos_profesores, name='ver_profesores'),
    path('read_instituciones', views.mostrar_datos_instituciones, name='ver_instituciones'),
    path('buscar_alumnos', views.buscar_alumnos, name='busqueda_alumnos'),
    path('buscar', views.buscar),
    path('opciones_busqueda', views.busqueda_opciones, name='opciones_busqueda'),
    path('buscar_profesores', views.buscar_profesores, name='busqueda_profesores'),
    path('buscar_instituciones', views.buscar_instituciones, name='busqueda_instituciones'),
    path('resultado_busqueda_alumno', views.resultado_busqueda_alumnos, name='resultado_alumnos'),
    path('resultado_busqueda_profesor',views.resultado_busqueda_profesores, name='resultado_profesores'),
    path('resultado_busqueda_instituciones', views.resultado_busqueda_instituciones, name='resultado_instituciones'),
    path('eliminar_alumno/<int:id>', views.eliminar_alumno, name="eliminar_alumno"),
    path('eliminar_profesor/<int:id>', views.eliminar_profesor, name="eliminar_profesor"),
    path('eliminar_institucion/<int:id>', views.eliminar_institucion, name="eliminar_institucion"),
    path("editar_alumno/<int:id>" , views.editar_alumno , name="editar_alumno"),
    path("editar_profesor/<int:id>" , views.editar_profesor , name="editar_profesor"),
    path("editar_institucion/<int:id>" , views.editar_institucion , name="editar_institucion"),
    path("login", views.login_request , name="login"),
    path("register", views.register , name="registrar"),
    path("bienvenido/", views.welcome, name='bienvenido'),
    path('logout', LogoutView.as_view(template_name="logout.html"), name='logout'),
    path('editar_perfil', views.editar_perfil , name='editar_perfil'),
    path('perfil_editado_confirmacion', views.editar_perfil_confirmacion, name='perfil_editado_confirmacion')
    
]