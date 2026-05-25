from fastapi import FastAPI
from pydantic import BaseModel
import mysql.connector

app = FastAPI()

class Clima(BaseModel):
    temperatura: float
    humedad: float
    presion: float

def get_connection():
    return mysql.connector.connect(
        host="db",
        user="root",
        password="123456",
        database="estacion_iot"
    )

@app.get("/")
def inicio():
    return {"mensaje": "API Estación Meteorológica IoT funcionando"}

@app.post("/data")
def recibir_datos(data: Clima):
    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    INSERT INTO clima (temperatura, humedad, presion)
    VALUES (%s, %s, %s)
    """

    cursor.execute(sql, (data.temperatura, data.humedad, data.presion))
    conn.commit()

    cursor.close()
    conn.close()

    return {
        "mensaje": "Datos guardados correctamente",
        "datos": data.dict()
    }

@app.get("/data")
def consultar_datos():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM clima ORDER BY fecha DESC LIMIT 50")
    resultados = cursor.fetchall()

    cursor.close()
    conn.close()

    return resultados