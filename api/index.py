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
def RouteIndex():
    return "Bienvenido!"

# Función Log-In
@app.route('/login', methods = ['POST'])
@cross_origin()
def login():
    rq = request.get_json()
    return jsonify(auth.autenticar(rq['username'], rq['password']))

# ROUTE MENU
@app.route('/altaPaciente', methods = ['POST', 'GET'])
@cross_origin()
def RouteAltaPaciente():
    rq = request.get_json()
    validado = auth.autenticar(rq['username'], rq['password'])
    if validado == True:
        rq = request.get_json()
        return altaPaciente.altaPaciente(rq['id'])
    return jsonify(False)
    
@app.route('/altaTurno', methods = ['POST', 'GET'])
@cross_origin()
def RouteAltaTurno():
    rq = request.get_json()
    validado = auth.autenticar(rq['username'], rq['password'])
    if validado == True: 
        rq = request.get_json()
        return altaTurno.altaTurno(rq['id'])
    return jsonify(False)

@app.route('/modificarPaciente', methods = ['POST', 'GET'])
@cross_origin()
def RouteModificarPaciente():
    rq = request.get_json()
    validado = auth.autenticar(rq['username'], rq['password'])
    if validado == True:
        rq = request.get_json() 
        # return editarPaciente(id)
    return jsonify(False)

@app.route('/listarTurnos', methods = ['POST', 'GET'])
@cross_origin()
def RouteListarTurnos():
    rq = request.get_json()
    validado = auth.autenticar(rq['username'], rq['password'])
    if validado == True: 
        return listarTurnos.listadoTurnos()
    return jsonify(False)

@app.route('/listarPacientes', methods = ['POST', 'GET'])
@cross_origin()
def RouteListarPacientes():
    rq = request.get_json()
    validado = auth.autenticar(rq['username'], rq['password'])
    if validado == True:
        return listarPacientes.listadoPacientes()
    return jsonify(False)

@app.route('/buscarTurnoSegunDni', methods = ['POST', 'GET'])
@cross_origin()
def RouteBuscarTurnoSegunDni():
    rq = request.get_json()
    validado = auth.autenticar(rq['username'], rq['password'])
    if validado == True:
        return buscarTurnoSegunDni.buscarTurno(rq['dni'])
    return jsonify(False)

@app.route('/agregarPaciente', methods = ['POST', 'GET'])
@cross_origin()
def RouteAgregarPaciente():
    rq = request.get_json()
    validado = auth.autenticar(rq['username'], rq['password'])
    if validado == True: 
        return "hola"
    return jsonify(False)

@app.route('/agregarTurno', methods = ['POST', 'GET'])
@cross_origin()
def RouteAgregarTurno():
    rq = request.get_json()
    validado = auth.autenticar(rq['username'], rq['password'])
    if validado == True: 
        return "hola"
    return jsonify(False)

@app.route('/testing', methods = ['POST', 'GET'])
@cross_origin()
def RouteTesting():
    rq = request.get_json()
    validado = auth.autenticar(rq['username'], rq['password'])
    if validado == True: 
        return "hola"
    return jsonify(False)

# API init
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=False)