import os
from flask import jsonify

os.system('cls')
db_path = os.path.dirname(os.path.abspath(__file__))

def listadoPacientes():
    fileUsuarios = open(os.path.abspath("api/db/usuarios"), 'r')
    usuarios = fileUsuarios.read()
    fileUsuarios.close()
    return jsonify(usuarios.split(";"))