#Comenzará su proyecto creando el código para determinar si una pieza de basura espacial es de un tamaño peligroso. Para este ejercicio utilizaremos un tamaño arbitrario de 5 metros cúbicos (5m3); cualquier cosa más grande es un objeto potencialmente peligroso.
object_max = 5
object_size = 25
if object_size > object_max:
    print("Necesitamos vigilar este objeto")
else:
    print("Este objeto no presenta una amenaza")