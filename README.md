# pg2_parcial_p2
# CineProject

Proyecto web desarrollado con Django para gestionar y mostrar información sobre películas.

## Descripción

Este proyecto es una aplicación básica en Django que tiene una página principal que muestra un mensaje de bienvenida. Es una base para agregar funcionalidades relacionadas con películas.

## Requisitos

- Python 3.8+
- Django 5.2.1 (u otra versión compatible)

## Instalación

1. Clona este repositorio o descarga el proyecto.

2. Crea y activa un entorno virtual:

```bash
python -m venv venv
source venv/bin/activate   # En Linux/macOS
venv\Scripts\activate      # En Windows PowerShell
Instala las dependencias:

bash
pip install django
Configuración
Asegúrate de que tu archivo cineproject/urls.py incluya la ruta a la aplicación peliculas:

python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('peliculas.urls')),  # Incluye urls de la app peliculas
]
En peliculas/urls.py define la ruta para la vista principal:

python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
En peliculas/views.py tienes la vista:

python
from django.http import HttpResponse

def home(request):
    return HttpResponse("¡Hola! Esta es la página principal de Películas.")
Ejecución
Para iniciar el servidor de desarrollo:

bash
python manage.py runserver
Luego abre en tu navegador:

cpp
http://127.0.0.1:8000/