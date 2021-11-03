import os
from flask import jsonify, Response, abort

bloqueoLogin = 0

def autenticar(username, password):
    global bloqueoLogin
    if bloqueoLogin < 3:
        try:
            fileUsuarios = open(os.path.abspath("api/db/usuarios"), 'r')
        except:
            return jsonify("FILE_NOT_FOUND")
        usuarios = fileUsuarios.read()
        fileUsuarios.close()
        arrUsuarios = usuarios.split(";")

        for usuario in arrUsuarios:
            if usuario.split(",")[1] == username and usuario.split(",")[2] == password:
                bloqueoLogin = 0
                return True
        
        bloqueoLogin += 1
        return False
    
    return "ACCESS_DENIED"
    