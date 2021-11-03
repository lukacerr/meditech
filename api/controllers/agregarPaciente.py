import os
import time
from flask import jsonify
from datetime import datetime

def pacienteRecursivo(file, dni):
    linea = file.readline()
    if not linea: file.close(); return False
    if dni == linea.split(",")[4]: file.close(); return True
    return pacienteRecursivo(file, dni)

def validaciones(nombre, apellido, edad):
    if len(nombre) < 3 or len(nombre) > 50:
        return False
    if len(apellido) < 2 or len(apellido) > 50:
        return False
    if 18 < int(edad) < 120:
        return False
    return True

def addPaciente(nombre, apellido, edad, dni):

    # Validación de DNI
    if pacienteRecursivo(open(os.path.abspath("api/db/pacientes"), 'r'), dni) == True:
        return jsonify("DNI_ALREADY_IN_USE")

    # Validaciones
    if validaciones(nombre, apellido, edad) == False:
        return jsonify('VALIDATION_ERROR')
    
    # ! ID
    file = open(os.path.abspath("api/db/pacientes"), "r")
    fileRead = file.readlines()
    file.close()

    with open(os.path.abspath("api/db/pacientes"), 'a') as file:
        if len(fileRead) > 0:
            # ! ID
            lastId = str(int(fileRead[len(fileRead)-1].split(",")[0]) + 1)
            file.write(f"\n{lastId},{nombre},{apellido},{edad},{dni};")
        else: file.write(f"1,{nombre},{apellido},{edad},{dni};")
        file.close()

    return jsonify("SUCCESS")