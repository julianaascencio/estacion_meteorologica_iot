# 🌦 Estación Meteorológica IoT Bogotá

Proyecto IoT para monitoreo ambiental en tiempo real usando:

- ESP32
- FastAPI
- MariaDB
- Docker
- Grafana
- Python

## Arquitectura

ESP32 / Simulador
        ↓
FastAPI REST API
        ↓
MariaDB
        ↓
Grafana Dashboard

## Características

✅ Monitoreo temperatura
✅ Monitoreo humedad
✅ Monitoreo presión
✅ Dashboard en tiempo real
✅ Simulación meteorológica Bogotá
✅ Dockerizado

## Tecnologías

Python
FastAPI
Docker
MariaDB
Grafana
ESP32

## Ejecución

docker compose up --build

Simulador:

py simulador.py

Dashboard:

http://localhost:3000

API:

http://localhost:8000

## Capturas

(aquí pondremos tus screenshots)

## Próximamente

Integración con sensores reales:

- DHT22
- BMP280
