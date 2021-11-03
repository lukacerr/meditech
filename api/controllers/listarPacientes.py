import os
from flask import jsonify

def pacienteRecursivo(file, listaPacientes):
    linea = file.readline()
    if linea == "": return "EMPTY_FILE"
    
    listaPacientes.append(linea.replace(";",""))
    pacienteRecursivo(file, listaPacientes)
     
    file.close()
    return listaPacientes

def listadoPacientes():
    return jsonify(pacienteRecursivo(open(os.path.abspath("api/db/pacientes"), 'r'), []))
    