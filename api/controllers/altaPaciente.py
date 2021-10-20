import os
from flask import jsonify

os.system('cls')
db_path = os.path.dirname(os.path.abspath(__file__))

def altaPaciente(id):
    fileUsuarios = open(os.path.abspath("api/db/usuarios"), 'r+')
    usuarios = fileUsuarios.read()
    arrUsuarios = usuarios.split(";")
    encontrado = False

    for usuario in arrUsuarios:
        if usuario.split(",")[0] != id:
            fileUsuarios.write(usuario)
        else:
            encontrado = True
    fileUsuarios.close()
    if encontrado:
        return jsonify("Paciente dado de alta con éxito! Ya no aparecerá más en la lista de usuarios.")
    else:
        return jsonify("Id del paciente recibido no es existente! Intente denuevo con otra id.")