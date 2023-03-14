# Se puede pasar varios argumentos a una función sin que estos esten definidos en la función.
# Para lograrlo usarmos un * antes del nombre del argumento en la función.
def variable_length(*args):
    print(args)

variable_length("One", "Two")

# Se puede de igual manera aceptar un sin número de argumentos de palabra clave (keyword arguments).
# Para lograrlo usamos doble ** antes del nombre del argumento.
def variable_length(**kwargs):
    print(kwargs)

variable_length(tanks=1, day="Wednesday", pilots=3)