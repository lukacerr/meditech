import os
from flask import jsonify

os.system('cls')
db_path = os.path.dirname(os.path.abspath(__file__))

def altaPaciente(id):
    encontrado = False;

    with open(os.path.abspath("api/db/pacientes"), "r") as file:
        lines = file.readlines()
        file.close()
    with open(os.path.abspath("api/db/pacientes"), "w") as file:
        for line in lines:
            if line.strip("\n").split(',')[0] != id:
                file.write(line)
            else: encontrado = True
        file.close()

    if encontrado: return jsonify("SUCCESS")
    return jsonify("NOT_FOUND")
