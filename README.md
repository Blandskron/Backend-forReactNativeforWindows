# Backend para React Native for Windows

Este repositorio contiene un backend desarrollado en Django para una aplicación React Native for Windows.

## Requisitos

- **Python 3.x**
- **pip** (el gestor de paquetes de Python)
- **Django 5.1.1**
- **Django Rest Framework 3.15.2**

## Instalación

Sigue los pasos a continuación para clonar y configurar el proyecto.

### 1. Clonar el repositorio

Primero, clona el repositorio en tu máquina local usando el siguiente comando en tu terminal:

```bash
git clone https://github.com/Blandskron/Backend-forReactNativeforWindows.git
```

Navega al directorio del proyecto:

```bash
cd Backend-forReactNativeforWindows
```

### 2. Crear y activar un entorno virtual (opcional, pero recomendado)

Para aislar las dependencias del proyecto, es recomendable usar un entorno virtual de Python. Puedes crear uno con los siguientes comandos:

```bash
# Crear el entorno virtual
python -m venv env

# Activar el entorno virtual
# En Windows
.\env\Scripts\activate
# En macOS/Linux
source env/bin/activate
```

### 3. Instalar las dependencias

Una vez dentro del directorio del proyecto, instala las dependencias listadas en el archivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Configurar la base de datos

El proyecto usa una base de datos SQLite de forma predeterminada, que no necesita configuraciones adicionales. Sin embargo, puedes cambiarla por una base de datos diferente en el archivo `settings.py` si es necesario.

Para preparar la base de datos y aplicar las migraciones, ejecuta los siguientes comandos:

```bash
python manage.py migrate
```

### 5. Ejecutar el servidor de desarrollo

Inicia el servidor de desarrollo de Django con el siguiente comando:

```bash
python manage.py runserver
```

El servidor debería estar corriendo en [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

### 6. API

Este backend está construido usando Django Rest Framework. Puedes interactuar con la API a través de las rutas expuestas en `urls.py`.

## Dependencias del Proyecto

Este proyecto utiliza las siguientes dependencias, que se pueden encontrar en el archivo `requirements.txt`:

- **asgiref==3.8.1**
- **Django==5.1.1**
- **djangorestframework==3.15.2**
- **sqlparse==0.5.1**
- **tzdata==2024.2**

## Contribuciones

Si deseas contribuir al proyecto, realiza un fork y envía un pull request con las mejoras o correcciones que hayas implementado.
