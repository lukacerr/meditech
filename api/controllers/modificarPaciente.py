import os
from flask import jsonify

os.system('cls')
db_path = os.path.dirname(os.path.abspath(__file__))

def obtenerPaciente(file, dni):
    linea = file.readline()
    if not linea: 
        file.close(); return False
    if dni == linea.split(",")[4].split(";")[0]: 
        file.close(); return linea
    return obtenerPaciente(file, dni)

def actualizarPaciente(file, dni, nombre, apellido, edad):
    linea = file.readline()
    if not linea:
        file.close(); return False
    if dni != linea.split(",")[4].split(";")[0]:
        file.write(linea)
    else:
        file.write(f"\n{linea.split(',')[0]},{dni},{nombre},{apellido},{edad};")
    return actualizarPaciente(file, dni, nombre, apellido, edad)
    
def recibirInformacion(dni):
    try:
        paciente = obtenerPaciente(open(os.path.abspath("api/db/pacientes"), 'r+'), dni)
        if paciente == False:
            return jsonify("DNI_INVALID")
        else:
            return jsonify(paciente)
    except:
        return jsonify("FILE_NOT_FOUND")

def modificarPaciente(dni, nombre, apellido, edad):
    pacienteActualizado = actualizarPaciente(open(os.path.abspath("api/db/pacientes"), 'r+'), dni, nombre, apellido, edad)
    if pacienteActualizado != False:
        return jsonify("SUCCESS")
    else:
        return jsonify("DATA_ERROR")