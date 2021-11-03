import os
import time
from flask import jsonify
from datetime import datetime
from collections import deque
from classes import Colas

def pacienteRecursivo(file, dni):
    linea = file.readline()
    if not linea: 
        file.close(); return False
    if dni == linea.split(",")[4].split(";")[0]: 
        file.close(); return True
    return pacienteRecursivo(file, dni)     
    
def validarHora(hora):
    hh, mm = hora.split(':')
    horaInt = int(mm) + 60*int(hh)
    if horaInt < 600 or horaInt > 840: return False
    else: return True

def validarFecha(fecha):
    d, m , y = fecha.split('/')
    if d in ['1', '01','8', '08','15','22']: return False
    else: return True

def addTurno(paciente, fecha, hora):
    # Validación de DNI
    if pacienteRecursivo(open(os.path.abspath("api/db/pacientes"), 'r'), paciente) == False:
        return jsonify("DNI_INVALID")
    
     # Validación de Fecha
    try: 
        datetime.strptime(fecha, '%d/%m/%Y')
        if validarFecha(fecha) == False:
            return jsonify('DATE_DISABLED')
    except: return jsonify("DATE_INVALID")

    # Validación de Hora
    try: 
        time.strptime(hora, '%H:%M')
        if validarHora(hora) == False:
            return jsonify('TIME_DISABLED')
    # Si no lo estuviesemos manejando enviando el resultado al frontend se ejecutaría un except de tipo 'Value Error'
    except: return jsonify("TIME_INVALID")

    file = open(os.path.abspath("api/db/turnos"), "r")
    count = len([line.strip("\n") for line in file if line != "\n"])
    file.close()

    # ! ID
    file = open(os.path.abspath("api/db/turnos"), "r")
    fileRead = file.readlines()
    file.close()
    
    cola = Colas.inicializar_cola()
    cola2 = []

    with open(os.path.abspath("api/db/turnos"), 'a') as file:
        if len(fileRead) > 0:
            # ! ID
            lastId = str(int(fileRead[len(fileRead)-1].split(",")[0]) + 1)
            cola2 = Colas.acolar(cola, f"\n{lastId},{paciente},{fecha},{hora};")
        else: file.write(f"1,{paciente},{fecha},{hora};")

        lenCola = len(cola2)
        if lenCola > 0:
            for i in range(lenCola):
                file.write(Colas.desacolar(cola2))
        file.close()
    
    return jsonify("SUCCESS")