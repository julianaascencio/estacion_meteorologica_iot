# Estación Meteorológica IoT Bogotá

Sistema de monitoreo ambiental en tiempo real basado en arquitectura IoT para la captura, almacenamiento, procesamiento y visualización de variables meteorológicas mediante infraestructura contenerizada, API REST y dashboard interactivo.

---

## Descripción del proyecto

Este proyecto implementa una estación meteorológica IoT orientada al monitoreo continuo de condiciones ambientales mediante sensores conectados a un microcontrolador ESP32.

El sistema permite capturar, almacenar y visualizar en tiempo real variables meteorológicas como:

- Temperatura ambiente
- Humedad relativa
- Presión atmosférica

La solución fue diseñada bajo una arquitectura modular y escalable, permitiendo integración con hardware IoT, backend desacoplado y visualización profesional para monitoreo en tiempo real.

---

## Arquitectura del sistema

```text
                +----------------------+
                |        ESP32         |
                |   Sensores IoT       |
                |   DHT22 / BMP280     |
                +----------+-----------+
                           |
                           | HTTP POST
                           v
                +----------------------+
                |    FastAPI REST API  |
                |    Endpoint /data    |
                +----------+-----------+
                           |
                           | SQL INSERT
                           v
                +----------------------+
                |   MariaDB Database   |
                |     Tabla clima      |
                +----------+-----------+
                           |
                           | Query
                           v
                +----------------------+
                |   Grafana Dashboard  |
                | Monitoreo en tiempo  |
                |        real          |
                +----------------------+
```

---

## Tecnologías utilizadas

### Backend
- Python 3
- FastAPI
- Uvicorn
- Pydantic

### Base de datos
- MariaDB 10.11

### Visualización
- Grafana

### Infraestructura
- Docker
- Docker Compose

### Hardware IoT
- ESP32
- Sensor DHT22
- Sensor BMP280

---

## Características principales

- Monitoreo ambiental en tiempo real
- API REST para recepción de datos IoT
- Persistencia de datos en base de datos SQL
- Dashboard interactivo con métricas históricas
- Arquitectura completamente dockerizada
- Integración modular entre hardware y software
- Visualización centralizada mediante Grafana
- Escalabilidad para futuras integraciones

---

## Estructura del proyecto

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
├── docker-compose.yml
└── README.md
```

---

## Endpoints disponibles

### Verificación del estado de la API

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

### Envío de datos meteorológicos

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

### Consulta de histórico

```http
GET /data
```

Permite recuperar registros almacenados en la base de datos.

---

## Instalación y despliegue

### Clonar el repositorio

```bash
git clone https://github.com/julianaascencio/estacion_meteorologica_iot.git
cd estacion_meteorologica_iot
```

---

### Levantar la infraestructura

```bash
docker compose up --build
```

Servicios disponibles:

API REST:

```text
http://localhost:8000
```

Dashboard Grafana:

```text
http://localhost:3000
```

Base de datos MariaDB:

```text
localhost:3306
```

---

## Dashboard de monitoreo

El dashboard desarrollado en Grafana permite visualizar:

- Temperatura actual
- Histórico de temperatura
- Humedad actual
- Histórico de humedad
- Presión atmosférica actual
- Histórico de presión atmosférica

Incluye actualización automática y monitoreo continuo.

---

## Mejoras futuras

- Integración completa con sensores físicos
- Alertas automáticas por umbrales críticos
- Notificaciones remotas
- Integración con MQTT
- Despliegue en nube
- Monitoreo multiestación
- Seguridad y autenticación de API

---

## Evidencia visual

Agregar capturas del dashboard en esta sección.

---

## Autor

Juliana Ascencio

Proyecto académico orientado a soluciones IoT para monitoreo ambiental.

GitHub:

https://github.com/julianaascencio

---

## Licencia

MIT License
