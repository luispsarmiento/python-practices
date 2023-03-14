# Creando una lista
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

# Accediendo a ciertos valores de la lista por medio de "índice"
print("The first planet is", planets[0])
print("The second planet is", planets[1])
print("The third planet is", planets[2])

# Modificación de un elemento en una lista
planets[3] = "Red Planet"
print("Mars is also known as", planets[3])

# Tamaño de una lista
number_of_planets = len(planets)
print("There are", number_of_planets, "planets in the solar system.")

# Es posible agregar nuevos valores a una lista por medio del método .append(value)
planets.append("Pluto")
number_of_planets = len(planets)
print("There are actually", number_of_planets, "planets in the solar system.")

# Eliminando valores de una lista
planets.pop()  # Goodbye, Pluto
number_of_planets = len(planets)
print("No, there are definitely", number_of_planets, "planets in the solar system.")

# Los índices negativos son una manera de acceder a elementos de la lista desde el último elemento al primero
print("The last planet is", planets[-1])
print("The penultimate planet is", planets[-2])

# Para conocer la posición que ocupa un elemento en la lista podemos usar el método index(value)
jupiter_index = planets.index("Jupiter")
print("Jupiter is the", jupiter_index + 1, "planet from the sun")
