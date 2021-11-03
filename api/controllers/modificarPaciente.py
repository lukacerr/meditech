import os
from flask import jsonify
from flask.scaffold import F

os.system('cls')
db_path = os.path.dirname(os.path.abspath(__file__))

def obtenerPaciente(file, dni):
    linea = file.readline()
    if not linea: 
        file.close(); return False
    if dni == linea.split(",")[4].split(";")[0]: 
        file.close(); return linea
    return obtenerPaciente(file, dni)

def actualizarPaciente(path, dni, nombre, apellido, edad):
    encontrado = False
    with open(path, "r") as file:
        lineas = file.readlines()
    with open(path, "w") as file:
        for linea in lineas:
            if dni+";" not in linea:
                file.write(linea)
            else: 
                encontrado = linea
                editado = linea.split(",")
                file.write(f"{editado[0]},{nombre},{apellido},{edad},{editado[4]}")
        file.close()
    return encontrado

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
    pacienteActualizado = actualizarPaciente(os.path.abspath("api/db/pacientes"), dni, nombre, apellido, edad)
    
    if pacienteActualizado != False:
        return jsonify("SUCCESS")
    
    return jsonify("DATA_ERROR")