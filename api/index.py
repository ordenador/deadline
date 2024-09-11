from datetime import datetime
from flask import Flask
import pytz

app = Flask(__name__)


def generar_barra_progreso_con_dias(fecha_inicio, fecha_actual, dias_totales):
    dias_transcurridos = (fecha_actual - fecha_inicio).days
    porcentaje = (dias_transcurridos / dias_totales) * 100
    ancho_maximo = 35
    progreso_simbolos = int((porcentaje / 100) * ancho_maximo)
    barra_whatsapp = '▓' * progreso_simbolos + '░' * (ancho_maximo - progreso_simbolos)
    return f"{barra_whatsapp}\n{porcentaje:.2f}% ({dias_transcurridos} de {dias_totales} días)"


@app.route('/')
def home():
    tz_santiago = pytz.timezone('America/Santiago')
    fecha_inicio = tz_santiago.localize(datetime(2024, 8, 14))
    fecha_actual = datetime.now(tz_santiago)
    dias_totales = 90
    barra_progreso = generar_barra_progreso_con_dias(fecha_inicio, fecha_actual, dias_totales)
    return f"<pre>{barra_progreso}</pre>"


if __name__ == "__main__":
    app.run(debug=True)
