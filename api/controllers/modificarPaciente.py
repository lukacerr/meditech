import os
from flask import jsonify

os.system('cls')
db_path = os.path.dirname(os.path.abspath(__file__))

def modificarPaciente(dni):
    try:
        filePacientes = open(os.path.abspath("api/db/pacientes"), 'r+')
    except:
        return jsonify("FILE_NOT_FOUND")
    pacientes = filePacientes.read()
    arrPacientes = pacientes.split(";")
    encontrado = False

    for paciente in arrPacientes:
        if paciente.split(",")[1] == dni:
            return jsonify(paciente)
    filePacientes.close()
    return jsonify("NOT_FOUND")