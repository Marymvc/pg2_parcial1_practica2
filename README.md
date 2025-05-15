# 📝 Parcial 1 - Programación II

**Nombre:** Mary Magali  
**Curso:** Técnico en Sistemas Informáticos  
**Materia:** Programación II  
**Fecha:** Mayo 2025

---

## 🎬 Proyecto Django: Cine

Este repositorio contiene un proyecto básico en Django para gestionar información sobre **películas** y **directores**. El sistema incluye modelos, panel de administración y un ejemplo cargado.

Repositorio: [pg2_parcial1_p2](https://github.com/Marymvc/pg2_parcial1_p2)

---

## ⚙️ Requisitos Técnicos

### 1. Crear entorno virtual

```bash
python -m venv venv
```

### 2. Activar entorno virtual

#### En Windows

```bash
.env\ScriptsActivate
```

#### En Linux / Mac

```bash
source venv/bin/activate
```

---

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

> Si no existe el archivo, podés crearlo con:

```bash
pip freeze > requirements.txt
```

---

### 4. Crear proyecto y aplicación

```bash
django-admin startproject cineproject
cd cineproject
python manage.py startapp cine
```

---

### 5. Configurar aplicación en `settings.py`

```python
# cineproject/settings.py

INSTALLED_APPS = [
    ...
    'cine',
]
```

---

## 🧱 Modelos

### cine/models.py

```python
from django.db import models

class Director(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.nombre

class Pelicula(models.Model):
    titulo = models.CharField(max_length=100)
    anio_estreno = models.IntegerField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name="peliculas")

    def __str__(self):
        return self.titulo
```

---

## 🔧 Migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 🛡️ Panel de administración

### cine/admin.py

```python
from django.contrib import admin
from .models import Director, Pelicula

admin.site.register(Director)
admin.site.register(Pelicula)
```

---

## 👤 Crear superusuario

```bash
python manage.py createsuperuser
```

---

## 🚀 Iniciar servidor

```bash
python manage.py runserver
```

---

## 📸 Capturas

Dentro del repositorio hay una carpeta `capturas/` con imágenes del panel de administración funcionando, donde se puede visualizar la gestión de películas y directores.

---

## 🔄 Subir cambios a GitHub

```bash
git add .
git commit -m "Primer commit - Proyecto Cine Django"
git push -u origin main  # o master si es tu rama principal
```

---