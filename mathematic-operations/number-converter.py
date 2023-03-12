# Al convertir cadenas en números, debe indicar el tipo de número que desea crear. Tiene que decidir si necesita un separador decimal. Se usa int para realizar la conversión en un número entero y float para hacerlo en un número de punto flotante.
demo_int = int('215')
print(demo_int)

demo_float = float('215.3')
print(demo_float)

# Para obtener el valor absoluto de una operación usaremos abs:
print(abs(39 - 16))
print(abs(16 - 39))

# Para redondear un número hacía arriba o hacia abajo usaremos la función integrada round
print(round(14.5))

# Biblioteca matemática para python es math, esta nos permite hacer operaciones y cálculso más avanzados.
# El redondeo de números permite quitar la parte decimal de un número de punto flotante. Puede optar por redondear siempre hacia arriba al número entero más cercano si usa ceil, o hacia abajo si usa floor.
from math import ceil, floor # aunque la importación de esta biblioteca la hacemos aquí en un programa más profesional siempre se hace al principio del contenido del archivo.

round_up = ceil(12.5)
print(round_up)

round_down = floor(12.5)
print(round_down)
