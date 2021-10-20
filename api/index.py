# Importes
import os
from flask import Flask, jsonify, request, url_for, redirect
from flask_cors import CORS, cross_origin
from controllers import altaPaciente, altaTurno, auth, buscarTurnoSegunDni, listarPacientes, listarTurnos, modificarPaciente, testing

# Inicializaciones
os.system('cls')
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# Rutas
@app.route('/', methods=["GET"])
@cross_origin()
def index():
    return "Bienvenido!"

# Función Log-In

@app.route('/login', methods = ['POST'])
def login():
    rq = request.get_json()
    return auth.autenticar(rq['username'], rq['password'])

# ROUTE MENU
@app.route('/menu/altaPaciente', methods = ['POST', 'GET'])
def bajaPaciente():
    validado = auth.autenticar(request.form['username'], request.form['password'])
    if validado == 'true':
        rq = request.get_json()
        return altaPaciente.altaPaciente(rq['id'])
    return False
    
@app.route('/menu/altaTurno', methods = ['POST', 'GET'])
def altaTurno():
    validado = auth.autenticar(request.form['username'], request.form['password'])
    if validado == 'true': 
        return "hola"
    return False

@app.route('/menu/modificarPaciente', methods = ['POST', 'GET'])
def modificarPaciente():
    validado = auth.autenticar(request.form['username'], request.form['password'])
    if validado == 'true': 
        return "hola"
    return False

@app.route('/menu/listarTurnos', methods = ['POST', 'GET'])
def listarTurnos():
    validado = auth.autenticar(request.form['username'], request.form['password'])
    if validado == 'true': 
        return True
    return False

@app.route('/menu/listarPacientes', methods = ['POST', 'GET'])
def listarPacientes():
    validado = auth.autenticar(request.form['username'], request.form['password'])
    if validado == 'true':
        return listarPacientes.listadoPacientes()
    return False

@app.route('/menu/buscarTurnoSegunDni', methods = ['POST', 'GET'])
def buscarTurnoSegunDni():
    validado = auth.autenticar(request.form['username'], request.form['password'])
    if validado == 'true': 
        return "hola"
    return False

@app.route('/menu/testing', methods = ['POST', 'GET'])
def testing():
    validado = auth.autenticar(request.form['username'], request.form['password'])
    if validado == 'true': 
        return "hola"
    return False

# API init
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=False)