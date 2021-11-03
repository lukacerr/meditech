import os
from flask import jsonify, Response, abort

bloqueoLogin = 0

def usuarioRecursivo(file, username, password):
    linea = file.readline()
    if not linea:
        file.close(); return False

    if username in linea and password in linea: 
        file.close(); return True

    return usuarioRecursivo(file, username, password)

def autenticar(username, password):
    global bloqueoLogin
    if bloqueoLogin < 3:
        login = usuarioRecursivo(open(os.path.abspath("api/db/usuarios"), 'r'), username, password)
        if login == True:
            bloqueoLogin = 0
            return True
        else:
            bloqueoLogin += 1
            return False
    
    return "ACCESS_DENIED"
    