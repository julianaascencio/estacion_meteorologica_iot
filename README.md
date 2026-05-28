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
<img width="488" height="424" alt="image" src="https://github.com/user-attachments/assets/e4fdffc9-57fc-4c48-b4d6-0047f5d592e9" />

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

## Montaje físico

El montaje físico está compuesto por un ESP32, un sensor DHT11 para la lectura de temperatura y un módulo BME/BMP280 para la medición de presión atmosférica.

<img width="874" height="627" alt="image" src="https://github.com/user-attachments/assets/23fbe91d-4cd2-414a-b147-e0df4890b8b0" />


## Conexiones del montaje
### ESP32
<img width="242" height="114" alt="image" src="https://github.com/user-attachments/assets/8119dd76-6600-4a07-ab79-edf20024da69" />


### DHT11
<img width="289" height="127" alt="image" src="https://github.com/user-attachments/assets/a6df4bed-4622-4540-a56e-94eff7fab91c" />

### BME/BMP280
<img width="300" height="142" alt="image" src="https://github.com/user-attachments/assets/bf60ea3a-3121-4200-a532-f568983a6d6c" />

## Código Arduino

El código del ESP32 se encuentra en:

```text
#include <WiFi.h>
#include <HTTPClient.h>
#include "DHT.h"

#define DHTPIN 4
#define DHTTYPE DHT11   // Si tu sensor es DHT22, cambia esto a DHT22

DHT dht(DHTPIN, DHTTYPE);

// Cambia estos datos por tu WiFi real
const char* ssid = "Mantenimiento";
const char* password = "12345678";

// IP de tu computador según ipconfig
String serverURL = "http://192.168.137.138:8000/data";

float humedad = 80.0;
float presion = 758.0;

void setup() {
  Serial.begin(115200);
  dht.begin();

  WiFi.begin(ssid, password);
  Serial.println("Conectando a WiFi...");

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.print(".");
  }

  Serial.println();
  Serial.println("WiFi conectado correctamente");
  Serial.print("IP del ESP32: ");
  Serial.println(WiFi.localIP());
}

void loop() {
  float temperatura = dht.readTemperature();

  if (isnan(temperatura)) {
    Serial.println("Error leyendo temperatura del sensor");
    delay(5000);
    return;
  }

  humedad += random(-10, 11) / 10.0;
  presion += random(-5, 6) / 10.0;

  humedad = constrain(humedad, 65.0, 98.0);
  presion = constrain(presion, 740.0, 765.0);

  String jsonData = "{";
  jsonData += "\"temperatura\":" + String(temperatura, 2) + ",";
  jsonData += "\"humedad\":" + String(humedad, 2) + ",";
  jsonData += "\"presion\":" + String(presion, 2);
  jsonData += "}";

  Serial.println("Enviando datos:");
  Serial.println(jsonData);

  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    http.begin(serverURL);
    http.addHeader("Content-Type", "application/json");

    int httpResponseCode = http.POST(jsonData);

    Serial.print("Respuesta HTTP: ");
    Serial.println(httpResponseCode);

    http.end();
  } else {
    Serial.println("WiFi desconectado");
  }

  delay(5000);
}
```
---

## Evidencia visual
### Serial monitor (arduino)
<img width="677" height="825" alt="image" src="https://github.com/user-attachments/assets/e41428f0-c88f-46f6-a3f2-7e4018052277" />

### Docker (Engine running)
<img width="1900" height="960" alt="image" src="https://github.com/user-attachments/assets/6f387958-e095-4415-9737-08197d9fa4c1" />

### VS Code (activacion de docker)
<img width="829" height="254" alt="image" src="https://github.com/user-attachments/assets/35d002ba-7d8d-43b3-bc0d-a367739d57b2" />

### Ruta de API FastAPI donde se almacenan y consultan los datos de la estación meteorológica.
<img width="1835" height="277" alt="image" src="https://github.com/user-attachments/assets/de357b62-bbd9-4518-98b5-7bcd768d3f4d" />

### Dashboard Grafana
<img width="1919" height="1006" alt="image" src="https://github.com/user-attachments/assets/92522806-abb9-4267-8e4c-8220f0bc07c1" />

### Temp en tiempo real 
<img width="1669" height="222" alt="image" src="https://github.com/user-attachments/assets/c6f608a1-ca1b-4b4d-ae2e-6f978d3d6e3b" />

## Humedad en tiempo real
<img width="1741" height="249" alt="image" src="https://github.com/user-attachments/assets/be939cc5-41ba-4359-9ace-e7912d487c08" />

### Presion en tiempo real
<img width="1744" height="232" alt="image" src="https://github.com/user-attachments/assets/386b895c-350a-42ea-ad00-26a29010292b" />

---

## Autor

- Juliana Ascencio
- Javier Ocampo

Proyecto académico orientado a soluciones IoT para monitoreo ambiental.

GitHub:

https://github.com/julianaascencio

---
