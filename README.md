# 📅 Gestor de Citas — Appointment Management System

Sistema web para la gestión de citas médicas o de servicios, desarrollado con Django y PostgreSQL, con una capa REST automática mediante PostgREST y despliegue completamente dockerizado.

---

## 🚀 Tecnologías

| Tecnología | Versión | Uso |
|---|---|---|
| 🐍 Python | 3.11+ | Lenguaje principal |
| 🎸 Django | 4.x | Framework backend |
| 🐘 PostgreSQL | 15+ | Base de datos relacional |
| 🔌 PostgREST | 11+ | API REST automática desde la BD |
| 🐳 Docker | 24+ | Contenedorización |
| 🐧 Linux (Ubuntu) | 22.04 | Sistema operativo base |

---

## ✨ Funcionalidades

- ✅ Registro y autenticación de usuarios
- ✅ Gestión de citas (crear, editar, cancelar, ver)
- ✅ Control de disponibilidad y detección de conflictos de horario
- ✅ Panel de administración con Django Admin
- ✅ API REST automática vía PostgREST
- ✅ Roles de usuario: administrador, profesional y cliente
- ✅ Notificaciones básicas de citas

---

## 🗂️ Estructura del Proyecto

```
Gestor-Citas-Django/
│
├── appointments/        # App principal de citas
├── users/               # App de autenticación y usuarios
├── config/              # Configuración del proyecto Django
├── docker/              # Archivos Docker y configuración
│   ├── nginx/
│   └── postgrest/
├── docker-compose.yml   # Orquestación de servicios
├── Dockerfile           # Imagen de la aplicación
├── requirements.txt     # Dependencias Python
├── manage.py
└── README.md
```

---

## ⚙️ Servicios Docker

| Servicio | Descripción | Puerto |
|---|---|---|
| `web` | Aplicación Django | `8000` |
| `db` | PostgreSQL | `5432` |
| `postgrest` | API REST automática | `3000` |

---

## 🛠️ Instalación y uso

### Requisitos previos

- [Docker](https://docs.docker.com/get-docker/) y Docker Compose instalados
- Git

### 1. Clonar el repositorio

```bash
git clone https://github.com/jaiber430/Gestor-Citas-Django.git
cd Gestor-Citas-Django
```

### 2. Configurar variables de entorno

```bash
cp .env.example .env
```

Edita el archivo `.env` con tus valores:

```env
SECRET_KEY=tu_clave_secreta
DEBUG=True
DB_NAME=gestor_citas
DB_USER=postgres
DB_PASSWORD=tu_password
DB_HOST=db
DB_PORT=5432
```

### 3. Levantar los servicios

```bash
docker compose up --build
```

### 4. Aplicar migraciones y crear superusuario

```bash
docker compose exec web python manage.py migrate
docker compose exec web python manage.py createsuperuser
```

### 5. Acceder a la aplicación

| Interfaz | URL |
|---|---|
| Aplicación web | http://localhost:8000 |
| Panel de administración | http://localhost:8000/admin |
| API PostgREST | http://localhost:3000 |

---

## 🔌 Uso de la API (PostgREST)

PostgREST expone automáticamente las tablas de PostgreSQL como endpoints REST.

```bash
# Listar citas
GET http://localhost:3000/appointments

# Filtrar por usuario
GET http://localhost:3000/appointments?user_id=eq.1

# Crear una cita
POST http://localhost:3000/appointments
Content-Type: application/json

{
  "user_id": 1,
  "date": "2025-05-15",
  "time": "10:00",
  "status": "pending"
}
```

---

## 🧪 Tests

```bash
docker compose exec web python manage.py test
```

---

## 📦 Dependencias principales

```txt
Django>=4.2
psycopg2-binary
djangorestframework
python-dotenv
gunicorn
```

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor abre un issue primero para discutir los cambios que deseas realizar.

1. Haz un fork del proyecto
2. Crea tu rama (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -m 'feat: agrega nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

---

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

---

## 👨‍💻 Autor

**Jaiber** — [@jaiber430](https://github.com/jaiber430)