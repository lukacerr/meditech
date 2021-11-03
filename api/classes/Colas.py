def inicializar_cola():
    cola = []
    return cola
    
def acolar(cola, dato):
    cola.insert(0, dato)
    return cola

def desacolar(cola):
    if len(cola) > 0:
        
        return cola.pop()
    else:
        raise ValueError('Cola vacía')
def primero(cola):
    if len(cola) > 0:
        return cola[-1]
    else:
        raise ValueError('Cola vacía')
def cola_vacia(cola):
    return len(cola) == 0