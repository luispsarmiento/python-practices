from datetime import date
import sys

print("Hello, World!")

#Fragmento de código con algunos tipos de datos
planets_in_solar_system = 8 # int, pluto used to be the 9th planet, but is too small
distance_to_alpha_centauri = 4.367 # float, lightyears
can_liftoff = True
shuttle_landed_on_the_moon = "Apollo 11" #string 

#La función type() ayuda a detectar que tipo de dato tiene cierta variable
print(type(distance_to_alpha_centauri))
#The output should be: <class 'float'>

#Python usa dos tipos de operadores: aritmético y asignación
#Aritmético: + - / *
#Asignación: = += -= /= (x /= 2) *= (x *= 2)
x = 2
x /= 2
print(x)
x *= 2
print(x)

#Para trabajar con fechas se debe importar el módulo date
print("Hoy es: " + str(date.today()))

#Recuperando argumentos de la línea de comandos
print(sys.argv)
print(sys.argv[1]) # program name
print(sys.argv[2]) # first arg

#Con input() podemos pedir datos al usuario
print("Welcome to the greeter program")
name = input("Enter your name: ")
print("Greetings " + name)

parsecs_input = input("Enter persecs: ")
lightyears = int(parsecs_input) * 3.26
print(str(parsecs_input) + " parsecs is " + str(lightyears) + " lightyears")