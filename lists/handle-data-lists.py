# En python puedo obtener segmentos de datos en una lista pasando el inicio y fin del segmento.
# Por ejemplo:
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
planets_before_earth = planets[0:2]
print(planets_before_earth)

# Para obtener un segmento de una determinada posición hasta el final de la lista podemos usar la siguiente instrucción:
planets_after_earth = planets[3:]
print(planets_after_earth)

# Para combinar listas en una usamos el operador +.
# Combinar las lunas de Jupiter de Amalthea y Galilean
amalthea_group = ["Metis", "Adrastea", "Amalthea", "Thebe"]
galilean_moons = ["Io", "Europa", "Ganymede", "Callisto"]

regular_satellite_moons = amalthea_group + galilean_moons
print("The regular satellite moons of Jupiter are", regular_satellite_moons)

# Se puede ordenar las listas usando el método .sort(), si sus valores son cadenas, se ordena alfabéticamente.
regular_satellite_moons.sort()
print("The regular satellite moons of Jupiter are", regular_satellite_moons)

# Para ordenar descendentemente usamos el parámetro reverse
regular_satellite_moons.sort(reverse=True)
print("The regular satellite moons of Jupiter are", regular_satellite_moons)
