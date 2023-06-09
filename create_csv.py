# Generar un archivo CSV con los datos de status.txt que nos indica si los trails estan abiertos o cerrados.
# El formao del archivo CSV es:
# status, blankets_creek, rope_mill
# "open", 0, 0
# "closed", 1, 1

def eliminar_duplicados():
    status_unicos = set()

    with open('status.txt', 'r') as f:
        for line in f.readlines():
            status_unicos.add(line.strip())

    # print()
    # print(len(status_unicos))
    return status_unicos

def limpiar_datos(statuses):
    status_limpio = []

    for status in statuses:
        linea = status.replace(',', ' ')
        linea = linea.replace('?', '')
        linea = linea.replace('!', '')
        linea = linea.replace('.', ' ')

        status_limpio.append(linea)
    
    return status_limpio

def normalizar_datos(statuses):
    status_normalizados = []

    for status in statuses:
        status_normalizados.append(status.lower())

    return status_normalizados

def identificar_status(statuses):
    valores = []

    for status in statuses:
        if "all trails are open" in status:
            valores.append([status, 1, 1])
        elif "all trails are closed" in status:
            valores.append([status, 0, 0])
        elif ""

def main():
    status_unicos = eliminar_duplicados()
    status_limpios = limpiar_datos(status_unicos)
    status_normalizados = normalizar_datos(status_limpios)

if __name__ == '__main__':
    main()