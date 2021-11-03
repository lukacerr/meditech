import os
from flask import jsonify

os.system('cls')
db_path = os.path.dirname(os.path.abspath(__file__))

def listadoPacientes():
    try:
        filePacientes = open(os.path.abspath("api/db/pacientes"), 'r')
    except:
        return jsonify("FILE_NOT_FOUND")
    pacientes = filePacientes.read()
    filePacientes.close()
    return jsonify(pacientes.split(";"))