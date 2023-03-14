# Creando un diccionario, un diccionario en python es a lo que en Javascript son objetos.
planet = {
    'name': 'Earth',
    'moons': 1
}

# Imprimiendo un valor de un diccionario:
print(planet.get('name'))
# planet['name'] is identical to using planet.get('name')
print(planet['name'])
# La diferencia entre .get y [] es que .get devuelve none si la clave no está disponible y [] lanza un error.

# Modificando valores de un diccionario
planet.update({'name': 'Makemake'})
planet['name'] = 'Makemake'

# Agregando nuevas claves
planet['orbital period'] = 4333

# Eliminando claves
planet.pop('orbital period')

# Se pueden anidar diccionarios, por ejemplo:
# Add address
planet['diameter (km)'] = {
    'polar': 133709,
    'equatorial': 142984
}

#Para recuperar valores en un diccionario anidado, debe encadenar corchetes o llamadas a get.
print(f'{planet["name"]} polar diameter: {planet["diameter (km)"]["polar"]}')
