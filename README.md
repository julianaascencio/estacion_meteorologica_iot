# 🌦 Estación Meteorológica IoT Bogotá

Sistema de monitoreo ambiental en tiempo real basado en arquitectura IoT, diseñado para la captura, almacenamiento, procesamiento y visualización de variables meteorológicas utilizando contenedores Docker, API REST y dashboard interactivo.

---

## 📌 Descripción del proyecto

Este proyecto implementa una **estación meteorológica IoT** capaz de monitorear variables ambientales como:

- 🌡 Temperatura ambiente
- 💧 Humedad relativa
- 🌀 Presión atmosférica

Actualmente el sistema opera con un **simulador meteorológico realista basado en condiciones de Bogotá, Colombia**, mientras se integran los sensores físicos.

La arquitectura fue diseñada para ser escalable, permitiendo reemplazar fácilmente el simulador por un **ESP32 con sensores reales (DHT22 y BMP280)** sin modificar el backend ni el dashboard.

---

# 🏗 Arquitectura del sistema

```text
                ┌────────────────────┐
                │ ESP32 / Simulador  │
                │ Datos meteorológicos│
                └─────────┬──────────┘
                          │ HTTP POST
                          ▼
                ┌────────────────────┐
                │ FastAPI REST API   │
                │ Endpoint /data     │
                └─────────┬──────────┘
                          │ SQL INSERT
                          ▼
                ┌────────────────────┐
                │ MariaDB Database   │
                │ Tabla clima        │
                └─────────┬──────────┘
                          │ Query
                          ▼
                ┌────────────────────┐
                │ Grafana Dashboard  │
                │ Visualización RT   │
                └────────────────────┘
```

---

# 🚀 Tecnologías utilizadas

## Backend
- Python 3
- FastAPI
- Uvicorn
- Requests
- Pydantic

## Base de datos
- MariaDB 10.11

## Visualización
- Grafana

## Infraestructura
- Docker
- Docker Compose

## IoT (próxima integración)
- ESP32
- DHT22
- BMP280

---

# ⚙ Características principales

✅ API REST para recepción de datos meteorológicos  
✅ Persistencia en base de datos SQL  
✅ Dashboard profesional en tiempo real  
✅ Simulación meteorológica basada en Bogotá  
✅ Arquitectura completamente dockerizada  
✅ Escalable a sensores físicos reales  
✅ Históricos de variables ambientales  
✅ Monitoreo continuo con actualización automática  

---

# 📂 Estructura del proyecto

```text
estacion_meteorologica_iot/
│
├── api/
│   ├── main.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── database/
│   └── init.sql
│
├── simulador.py
├── docker-compose.yml
└── README.md
```

---

# 🔌 Endpoints disponibles

## API principal

### Verificar estado

```http
GET /
```

Respuesta:

```json
{
  "mensaje": "API Estación Meteorológica IoT funcionando"
}
```

---

### Enviar datos meteorológicos

```http
POST /data
```

Ejemplo:

```json
{
  "temperatura": 14.6,
  "humedad": 81.2,
  "presion": 758.4
}
```

---

### Consultar histórico

```http
GET /data
```

---

# 🐳 Instalación y ejecución

## 1. Clonar repositorio

```bash
git clone https://github.com/julianaascencio/estacion_meteorologica_iot.git
cd estacion_meteorologica_iot
```

---

## 2. Levantar contenedores

```bash
docker compose up --build
```

Servicios disponibles:

FastAPI:

```text
http://localhost:8000
```

Grafana:

```text
http://localhost:3000
```

MariaDB:

```text
localhost:3306
```

---

# 🌆 Simulación meteorológica Bogotá

Mientras se integran sensores físicos, el sistema utiliza un simulador de condiciones reales nocturnas de Bogotá:

- Temperatura: 8°C – 18°C
- Humedad: 65% – 98%
- Presión atmosférica: 740 – 765 hPa

Ejecutar:

```bash
py simulador.py
```

Esto enviará datos automáticos cada 5 segundos al backend.

---

# 📊 Dashboard Grafana

El dashboard incluye:

- 🌡 Temperatura actual
- 📈 Histórico de temperatura
- 💧 Humedad actual
- 📈 Histórico de humedad
- 🌀 Presión actual
- 📈 Histórico de presión

Con actualización automática en tiempo real.

---

# 🧠 Futuras mejoras

## Integración hardware real
- ESP32
- Sensor DHT22
- Sensor BMP280

## Mejoras funcionales
- Alertas automáticas
- Notificaciones MQTT
- Dashboard remoto
- Autenticación de API
- Despliegue en nube
- Monitoreo multiestación

---

# 📷 Capturas del dashboard

Agregar aquí screenshots del dashboard:

```text
/images/dashboard.png
```

---

# 👨‍💻 Autor

**Juliana Ascencio**

Proyecto académico / portafolio IoT.

GitHub:

https://github.com/julianaascencio

---

# 📄 Licencia

MIT License
