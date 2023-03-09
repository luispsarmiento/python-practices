#Al crear instrucciones if más complejas podemos ayudarnos de else y elif.
#Por ejemplo, si desea que una condición responda a una prueba TRUE y FALSE, podría escribir lo siguiente:
a = 93
b = 27
if a >= b:
    print(a)
else:
    print(b)

#Sí desea crear una instrucción if de multiples pruebas puede ayudarse con la palabra clave elif.
#Analice el siguiente ejemplo:
a = 93
b = 27
if a >= b:
    print("a is greater than or equal to b")
elif a == b:
    print("a is equal to b")

#Puede combinar if, elif y else para crear programas con lógica condicional compleja.
#Por ejemplo:
a = 93
b = 27
if a > b:
    print("a is greater than b")
elif a < b:
    print("a is less than b")
else: 
    print ("a is equal to b")

#Uso de la lógica condicional anidada. 
#Para anidar condiciones, aplique sangría a las condiciones internas 
# y todo lo que esté en el mismo nivel de sangría se ejecutará en el mismo bloque de código:
a = 16
b = 25
c = 27
if a > b:
    if b > c:
        print ("a is greater than b and b is greater than c")
    else: 
        print ("a is greater than b and less than c")
elif a == b:
    print ("a is equal to b")
else:
    print ("a is less than b")