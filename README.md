# 📌 API de Gestión de Tareas - Cristian

Este proyecto es una API REST desarrollada con Django y Django REST Framework para la gestión de tareas personales. Incluye autenticación JWT, paginación, filtros, relaciones entre usuarios y tareas, y pruebas unitarias.

## 📦 Requisitos

- Python 3.10 o superior
- Django 4.x
- Django REST Framework
- SimpleJWT
- django-filter
- Postman (para pruebas manuales)

## ⚙️ Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/cristianr02020/apiproyectocdrc.git
```

2. Navega al proyecto:
```bash
cd api_proyecto
```

3. Crea un entorno virtual y actívalo:
```bash
python -m venv env
env\Scripts\activate  # En Windows
source env/bin/activate  # En Linux/macOS
```

4. Instala las dependencias:
```bash
pip install -r requirements.txt
```

5. Aplica migraciones:
```bash
python manage.py migrate
```

6. Crea un superusuario:
```bash
python manage.py createsuperuser
```

7. Ejecuta el servidor:
```bash
python manage.py runserver
```

## Endpoints Principales

| Método | Endpoint            | Descripción                       |
|--------|---------------------|-----------------------------------|
| POST   | /api/token/         | Obtener token JWT                 |
| POST   | /api/token/refresh/ | Refrescar token JWT               |
| GET    | /tareas/            | Listar tareas (requiere login)    |
| POST   | /tareas/            | Crear una nueva tarea             |
| GET    | /tareas/{id}/       | Ver detalles de una tarea         |
| PUT    | /tareas/{id}/       | Actualizar tarea                  |
| DELETE | /tareas/{id}/       | Eliminar tarea                    |

## Filtros

Puedes filtrar las tareas por nombre:
```
GET /tareas/?nombre=Estudiar
```

## 🔐 Autenticación

Usamos JWT con `SimpleJWT`. Para autenticarte:

1. Haz un `POST` a `/api/token/` con tus credenciales:
```json
{
  "username": "cristian",
  "password": "12345678"
}
```

2. Usa el token en las siguientes peticiones:
```
Authorization: Bearer tu_token
```

## Pruebas con Postman

Ejemplos incluidos en la colección `postman_collection.json` (si se subió al repositorio).

Pruebas mínimas recomendadas:
- Autenticación con JWT.
- Crear tarea autenticado.
- Ver tareas filtradas.
- Evitar creación sin token.

## Pruebas Unitarias

En `tareas/tests.py` se incluyen pruebas básicas como:

- Verificar creación de tareas con usuario autenticado.
- Verificar que un usuario no autenticado no puede crear tareas.

Para ejecutar:
```bash
python manage.py test
```

## Autor

- Cristian Romero 
