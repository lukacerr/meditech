import os
from flask import jsonify

def turnosRecursivo(file, listaTurnos):
    linea = file.readline()
    if linea == "": return "EMPTY_FILE"
    
    listaTurnos.append(linea.replace(";",""))
    turnosRecursivo(file, listaTurnos)
     
    file.close()
    return listaTurnos

def listadoTurnos():
    return jsonify(turnosRecursivo(open(os.path.abspath("api/db/turnos"), 'r'), []))
    