import os
from flask import jsonify

os.system('cls')
db_path = os.path.dirname(os.path.abspath(__file__))

def altaPaciente(id):
    try:
        filePacientes = open(os.path.abspath("api/db/pacientes"), 'r+')
    except:
        return jsonify("FILE_NOT_FOUND")
    pacientes = filePacientes.read()
    arrPacientes = pacientes.split(";")
    encontrado = False

    for paciente in arrPacientes:
        if pacientes.split(",")[0] != id:
            filePacientes.write(paciente)
        else:
            encontrado = True
    filePacientes.close()
    if encontrado:
        return jsonify("Paciente dado de alta con éxito! Ya no aparecerá más en la lista de pacientes.")
    else:
        return jsonify("Id del paciente recibido no es existente! Intente denuevo con otra id.")