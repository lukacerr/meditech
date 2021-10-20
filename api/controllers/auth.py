import os
from flask import jsonify, Response, abort

bloqueoLogin = 0

def autenticar(username, password):
    global bloqueoLogin
    if bloqueoLogin < 3:
        fileUsuarios = open(os.path.abspath("api/db/usuarios"), 'r')
        usuarios = fileUsuarios.read()
        fileUsuarios.close()
        arrUsuarios = usuarios.split(";")

        for usuario in arrUsuarios:
            if usuario.split(",")[1] == username and usuario.split(",")[2] == password:
                return jsonify(True)
        
        bloqueoLogin += 1
        return jsonify(False)
    else:
        # status_code = Response(status=403)
        abort(403, description="access_denied")

    return jsonify(False)
