from flask import Flask
from datetime import datetime

app = Flask(__name__)

def generar_barra_progreso_con_dias(fecha_inicio, fecha_actual, dias_totales):
    # Calcular días transcurridos
    dias_transcurridos = (fecha_actual - fecha_inicio).days
    
    # Calcular el porcentaje de progreso
    porcentaje = (dias_transcurridos / dias_totales) * 100
    
    # Ajustar el cálculo para una barra de 35 caracteres
    ancho_maximo = 35
    progreso_simbolos = int((porcentaje / 100) * ancho_maximo)
    
    # Crear la barra de progreso con caracteres estilo WhatsApp
    barra_whatsapp = '▓' * progreso_simbolos + '░' * (ancho_maximo - progreso_simbolos)
    
    # Mostrar la barra, el porcentaje y los días transcurridos
    return f"{barra_whatsapp}\n{porcentaje:.2f}% ({dias_transcurridos} de {dias_totales} días)"

@app.route('/')
def home():
    # Configuración para la barra de progreso
    fecha_inicio = datetime(2024, 8, 14)
    fecha_actual = datetime.now()  # Utilizar la fecha actual
    dias_totales = 90

    # Generar la barra de progreso
    barra_progreso = generar_barra_progreso_con_dias(fecha_inicio, fecha_actual, dias_totales)

    # Retornar la barra como texto
    return f"<pre>{barra_progreso}</pre>"
