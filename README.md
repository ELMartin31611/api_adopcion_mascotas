# 🐾 API de Adopción de Mascotas

Backend desarrollado con Django REST Framework para gestionar una aplicación de adopción de mascotas.

Incluye autenticación JWT, CRUD completo, filtros, paginación y conexión a PostgreSQL.

---

## 🚀 Tecnologías usadas

- Python 3.x
- Django
- Django REST Framework
- PostgreSQL
- JWT (SimpleJWT)
- django-filter
- python-decouple

---

## ⚙️ Instalación del proyecto

### 1. Clonar repositorio

git clone https://github.com/tu-usuario/api_adopcion_mascotas.git
cd api_adopcion_mascotas

---

### 2. Crear entorno virtual

python -m venv .venv
source .venv/bin/activate  # Linux / Mac
.venv\Scripts\activate     # Windows

---

### 3. Instalar dependencias

pip install -r requirements.txt

---

### 4. Configurar variables de entorno

Crear archivo `.env` en la raíz:

SECRET_KEY=clave_super_segura
DEBUG=True

DB_NAME=adopcion
DB_USER=postgres
DB_PASSWORD=1234
DB_HOST=localhost
DB_PORT=5432

---

### 5. Migraciones

python manage.py makemigrations
python manage.py migrate

---

### 6. Ejecutar servidor

python manage.py runserver

Servidor disponible en:

http://127.0.0.1:8000/api/

---

## 🔐 Autenticación (JWT)

### Registro

POST /api/auth/register/

Body:

{
  "username": "admin",
  "password": "admin"
}

---

### Login

POST /api/auth/login/

Respuesta:

{
  "access": "TOKEN",
  "refresh": "TOKEN"
}

---

### Uso del token

Agregar en headers:

Authorization: Bearer TU_ACCESS_TOKEN

---

## 📦 Endpoints disponibles

### 🔐 Auth
- POST /api/auth/register/
- POST /api/auth/login/
- POST /api/auth/token/refresh/
- POST /api/auth/token/verify/
- POST /api/auth/logout/

---

### 🏢 Fundaciones
- GET /api/fundaciones/
- POST /api/fundaciones/
- GET /api/fundaciones/{id}/
- PATCH /api/fundaciones/{id}/
- DELETE /api/fundaciones/{id}/

---

### 🐶 Mascotas
- GET /api/mascotas/
- POST /api/mascotas/
- GET /api/mascotas/{id}/
- PATCH /api/mascotas/{id}/
- DELETE /api/mascotas/{id}/

---

### 📋 Solicitudes
- GET /api/solicitudes/
- POST /api/solicitudes/
- GET /api/solicitudes/{id}/
- PATCH /api/solicitudes/{id}/
- DELETE /api/solicitudes/{id}/

---

### 🐾 Rescates
- GET /api/rescates/
- POST /api/rescates/
- GET /api/rescates/{id}/
- PATCH /api/rescates/{id}/
- DELETE /api/rescates/{id}/

---

### 💰 Donaciones
- GET /api/donaciones/
- POST /api/donaciones/
- GET /api/donaciones/{id}/
- PATCH /api/donaciones/{id}/
- DELETE /api/donaciones/{id}/

---

## 🔎 Filtros y búsqueda

Todos los endpoints soportan:

### 🔍 Búsqueda
/api/mascotas/?search=perro

### 📊 Ordenamiento
/api/mascotas/?ordering=nombre
/api/mascotas/?ordering=-created_at

### 📄 Paginación
/api/mascotas/?page=1

---

## 🧪 Ejemplo completo (flujo real)

### 1. Login

POST /api/auth/login/

### 2. Usar token

Authorization: Bearer TOKEN

### 3. Crear fundación

POST /api/fundaciones/

{
  "nombre": "Huellitas",
  "direccion": "Quito",
  "telefono": "0999999999",
  "correo": "test@test.com",
  "descripcion": "Rescate animal"
}

---

### 4. Crear mascota

POST /api/mascotas/

{
  "nombre": "Max",
  "especie": "Perro",
  "edad": 2,
  "fundacion": 1
}

---

### 5. Crear solicitud

POST /api/solicitudes/

{
  "usuario": 1,
  "mascota": 1,
  "estado": "pendiente"
}

---

## 📮 Colección Postman

Se incluye colección completa con:

- Auth
- Fundaciones
- Mascotas
- Solicitudes
- Rescates
- Donaciones

Importar en Postman y configurar:

base_url = http://localhost:8000/api

---

## 📁 Estructura del proyecto

store/
├── models/
├── serializers/
├── views/
├── filters.py
├── permissions.py
├── pagination.py
└── urls.py

---

## ✅ Evaluación cumplida

✔ Backend funcional con PostgreSQL  
✔ CRUD completo  
✔ Autenticación JWT  
✔ Permisos implementados  
✔ Filtros y paginación  
✔ Documentación completa  

---

## 👨‍💻 Autor

Proyecto académico — Desarrollo de API REST