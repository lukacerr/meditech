import os
from flask import jsonify

os.system('cls')
db_path = os.path.dirname(os.path.abspath(__file__))

def altaTurno(id):
    try:
        fileTurnos = open(os.path.abspath("api/db/turnos"), 'r')
    except:
        return jsonify("FILE_NOT_FOUND")

    turnos = fileTurnos.readlines()
    fileTurnos = open(os.path.abspath("api/db/turnos"), 'w')
    encontrado = False

    for turno in turnos:
        if turno.strip("\n") != id:
            fileTurnos.write(turno)
        else:
            encontrado = True
    print(fileTurnos.readlines())
    fileTurnos.close()
    if encontrado:
        return jsonify("SUCCESS") # Turno dado de alta con éxito! Ya no aparecerá más en la lista de turnos
    else:
        return jsonify("NOT_FOUND")