# Python incluye varios métodos de cadena diseñados para realizar las transformaciones más comunes y útiles.
# Los métodos de cadena forman parte del tipo str.
to_title = "temperatures and facts about the moon".title()
print(to_title)

temperatures = """Daylight: 260 F
Nighttime: -280 F"""
# split() sin argumentos, el método separará la cadena en cada espacio
print(temperatures.split())
print(temperatures.split("\n"))

# Buscar una cadena
# La manera más sencilla de detectar si existe una palabra, un carácter o un grupo de caracteres determinados en una cadena es usar el operador in:
exist = "Moon" in "This text will describe facts about the Moon"
print(exist)

# Un enfoque para buscar la posición de una palabra específica en una cadena consiste en usar el método .find():
temperatures = """Saturn has a daytime temperature of -170 degrees Celsius,
while Mars has -28 Celsius."""
index = temperatures.find("Moon")
print(index)

# Transformación de cadenas a mayúsculas y minúsculas
sentence = "The Moon And The Earth"
print(sentence.lower())
print(sentence.upper())

# Python tiene métodos que ayudan a comprobar el tipo de cadena:
mars_temperature = "The highest temperature on Mars is about 30 C"
for item in mars_temperature.split():
    if item.isnumeric():
        print(item)