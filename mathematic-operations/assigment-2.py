# Crear un programa que permita cálcula la distancia entre dos planetas cuyas distancias sea proporcionado por el usuario:
first_planet_input = input('Enter the distance from the sun for the first planet in KM: ')
second_planet_input = input('Enter the distance from the sun for the second planet in KM: ')

first_planet = int(first_planet_input)
second_planet = int(second_planet_input)

distance_km = abs(second_planet - first_planet)
print("The distance is: " + str(distance_km))