"""proyecto001 Configuración URL

La lista `urlpatterns` enruta las URL a las vistas. Para obtener más información, consulte:
     https://docs.djangoproject.com/en/3.0/topics/http/urls/
Ejemplos:
Vistas de función
     1. Agregue una importación: desde las vistas de importación de my_app
     2. Agregue una URL a urlpatterns: ruta ('', vistas.inicio, nombre = 'inicio')
Vistas basadas en clases
     1. Agregue una importación: from other_app.views import Home
     2. Agrega una URL a urlpatterns: ruta('', Inicio.as_view(), nombre='inicio')
Incluir otra URLconf
     1. Importe la función include(): desde django.urls import include, ruta
     2. Agrega una URL a urlpatterns: ruta('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from miapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("inicio/", views.index, name="inicio"),
    path("saludo/", views.saludo, name="saludo"),
    path("rango/", views.rango, name="rango"),
    path("rango2/", views.rango2, name="rango2"),
    path("rango2/<int:a>", views.rango2, name="rango2"),
    path("rango2/<int:a>/<int:b>", views.rango2, name="rango2"),
]
