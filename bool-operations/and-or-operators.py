# Los operadores AND y OR nos sirven para componer una condición.
# Por ejemplo:

a = 23
b = 34
if a == 34 or b == 34:
    print(a + b)

a = 23
b = 34
if a == 34 and b == 34:
    print (a + b)

# Para poder identificar la diferencia entre los dos operadores, puede usar la siguiente tabla de verdad:
# Tabla de verdad para AND
# subexpression1    |   Operador    |   subexpression2  |   Resultado
# -------------------------------------------------------------------
# True              |   and         |   True            |   True
# True              |   and         |   False           |   False
# False             |   and         |   True            |   False
# False             |   and         |   False           |   False

# Tabla de verdad para OR
# subexpression1    |   Operador    |   subexpression2  |   Resultado
# -------------------------------------------------------------------
# True              |   or          |   True            |   True
# True              |   or          |   False           |   True
# False             |   or          |   True            |   True
# False             |   or          |   False           |   False