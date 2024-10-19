from flask import Flask, request, jsonify, redirect
import requests

app = Flask(__name__)

# Microservicios
MICROSERVICE_1_URL = "https://microservicio1.onrender.com"
MICROSERVICE_2_URL = "https://microservicio2.onrender.com"

# Redirige las solicitudes a la raíz al Microservicio 1
@app.route('/')
def home():
    try:
        # Redirigir la solicitud al Microservicio 1 (Publicaciones)
        response = requests.get(f"{MICROSERVICE_1_URL}/")
        return response.content, response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Redirige las solicitudes de autenticación al Microservicio 2
@app.route('/autenticacion/<path:path>', methods=['GET', 'POST'])
def autenticacion(path):
    try:
        if request.method == 'POST':
            # Redirige las solicitudes POST al Microservicio 2
            response = requests.post(f"{MICROSERVICE_2_URL}/autenticacion/{path}", data=request.form)
        else:
            # Redirige las solicitudes GET al Microservicio 2
            response = requests.get(f"{MICROSERVICE_2_URL}/autenticacion/{path}")
        return response.content, response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Redirige las solicitudes de dashboard al Microservicio 2
@app.route('/dashboard')
def dashboard():
    try:
        # Redirigir la solicitud al Microservicio 2 (Dashboard)
        response = requests.get(f"{MICROSERVICE_2_URL}/dashboard")
        return response.content, response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Redirige las solicitudes de registro de usuario al Microservicio 2
@app.route('/autenticacion/registro-usuario', methods=['GET', 'POST'])
def registro_usuario():
    try:
        if request.method == 'POST':
            # Redirige las solicitudes POST (cuando el usuario se registra)
            response = requests.post(f"{MICROSERVICE_2_URL}/autenticacion/registro-usuario", data=request.form)
        else:
            # Redirige las solicitudes GET (cuando se carga la página de registro)
            response = requests.get(f"{MICROSERVICE_2_URL}/autenticacion/registro-usuario")
        return response.content, response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
