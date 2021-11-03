import os
from flask import json, jsonify

os.system('cls')
db_path = os.path.dirname(os.path.abspath(__file__))

def turnosRecursivo(file, listaTurnos, dni):
    linea = file.readline()
    if not linea: return "EMPTY_FILE"
    
    if linea.split(",")[1] == dni: listaTurnos.append(linea.replace(";",""))
    turnosRecursivo(file, listaTurnos, dni)
     
    file.close()
    return listaTurnos

def buscarTurno(dni):
    turnos = turnosRecursivo(open(os.path.abspath("api/db/turnos"), 'r'), [], dni)
    if len(turnos) == 0: return jsonify("NOT_FOUND")
    # El front lo lee como string separado por ;
    return jsonify(';'.join(turnos))
    
    