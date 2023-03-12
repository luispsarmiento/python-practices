# Puede hacer una división y redondear hacía bajo el resultado:
seconds = 1042
display_minutes = 1042 // 60
print(display_minutes)

# Encontrar el resto de una división con el operador módulo (%)
display_seconds = 1042 % 60
print(display_seconds)

# Las operaciones matemáticas en python se evaluan en este orden
# 1.- Paréntesis
# 2.- Exponentes
# 3.- Multiplicación y división
# 4.- Suma y resta
result_1 = 1032 + 26 * 2
result_2 = 1032 + (26 * 2)
# The answer is the same in both cases - 1084
print(result_1)
print(result_2)