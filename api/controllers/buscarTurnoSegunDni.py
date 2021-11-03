import os
from flask import jsonify

os.system('cls')
db_path = os.path.dirname(os.path.abspath(__file__))

def buscarTurno(dni):
    try:
        fileTurnos = open(os.path.abspath("api/db/turnos"), 'r+')
    except:
        return jsonify("FILE_NOT_FOUND")
    turnos = fileTurnos.read()
    arrTurnos = turnos.split(";")
    turnosFound = ""
    encontrado = False

    for turno in arrTurnos:
        if turno.split(",")[1] == dni:
            encontrado = True
            if turnosFound == "":
                turnosFound += turno
            else:
                turnosFound += ";" + turno
    
    fileTurnos.close()
    if encontrado: return jsonify(turnosFound)
    return jsonify("NOT_FOUND")
    
    
    