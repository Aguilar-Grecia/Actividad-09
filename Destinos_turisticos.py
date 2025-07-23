clientes = {}
def contar_la_lista (lista, i=0):
    try:
        lista[i]
        return 1 + contar_la_lista(lista, i + 1)
    except ValueError:
        return 0

def destinos_totales(claves, i=0):
    try:
        clave = claves[i]
        destinos = clientes[clave]["destino"]
        return contar_la_lista(destinos) + destinos_totales(claves, i + 1)
    except ValueError:
        return 0
def clientes_con_mas_destinos_visitados(claves, i=0, max_nombre= " ", max_cantidad =0):
    try:
        clave = claves[i]
        nombre = clientes[clave]["nombre"]
        destinos = clientes[clave]["destino"]
        cantidad_actual = contar_la_lista(destinos)
        if cantidad_actual > max_cantidad :


