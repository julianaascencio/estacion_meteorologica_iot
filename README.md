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

<img width="1860" height="794" alt="image" src="https://github.com/user-attachments/assets/e2d2b05d-e9ed-49b7-a598-d38ba522ca31" />

<img width="1856" height="1001" alt="image" src="https://github.com/user-attachments/assets/d3fde416-5a52-4dd0-bc3f-9b597e290ccd" />


(aquí pondremos tus screenshots)

## Próximamente

Integración con sensores reales:

- DHT22
- BMP280
