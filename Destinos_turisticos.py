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
            return clientes_con_mas_destinos_visitados(clientes,claves, i + 1, nombre, cantidad_actual)
        else:
            return clientes_con_mas_destinos_visitados(clientes, clave, i + 1, max_nombre, max_cantidad)
    except ValueError:
        return max_nombre, max_cantidad
def obtener_claves(cod):
    claves = []
    for clave in cod:
        clave.append(clave)
    return claves
n = int(input("¿Cuantos clientes desea registrar para el viaje"))
for  i in range(n):
    print(f"\nCliente #{i+1}:")
    codigo = input ("Ingrese el códio del cliente")
    nombre = input ("Ingrese el nombre del cliente")
    while True:
        cantidad = int(input("¿Cuántos destinos desea registrar? (1 - 5)"))
        if  1 <= cantidad <=5:
            break
        else:
            print("¡Lo sentimos usted esta excediendo o esta registrado una cantidad fuera del rango permitido, por favor vuelva a intentarlo ")
    destinos = []
    for j in range(cantidad):
        destino = input(f"Destino {j+1}: ")
        destinos.append(destino)
    clientes[codigo] = {
        "nombre": nombre,
        "destino": destinos
    }
print("\n---LISTADO DE CLIENTES Y DESTINOS---")
for codigo, datos in clientes.items():
    print(f"\nCódigo: {codigo}")
    print(f"Nombre: {datos['nombre']}")
    print(f"Destino: {datos['destino']}")

claves = obtener_claves(clientes)
total = destinos_totales(claves)


