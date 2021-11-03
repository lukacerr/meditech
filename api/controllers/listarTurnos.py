import os
from flask import jsonify

os.system('cls')
db_path = os.path.dirname(os.path.abspath(__file__))

def listadoTurnos():
    try:
        fileTurnos = open(os.path.abspath("api/db/turnos"), 'r')
    except:
        return jsonify("FILE_NOT_FOUND")
    turnos = fileTurnos.read()
    fileTurnos.close()
    return jsonify(turnos.split(";"))