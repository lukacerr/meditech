import os
from flask import jsonify

def altaTurno(id):
    encontrado = False;
    
    with open(os.path.abspath("api/db/turnos"), "r") as file:
        lines = file.readlines()
        file.close()
    with open(os.path.abspath("api/db/turnos"), "w") as file:
        for line in lines:
            if line.strip("\n").split(',')[0] != id:
                file.write(line)
            else: encontrado = True
        file.close()

    if encontrado: return jsonify("SUCCESS")
    return jsonify("NOT_FOUND")