# En Python, las cadenas son inmutables. Es decir, no pueden cambiar.
fact = 'The Moon has no atmosphere.'
fact + " No sound can be heard on the Moon."
print(fact)
# Al agregar cadenas, Python no modifica ninguna, sino que devuelve una cadena nueva como resultado. Para mantener este resultado nuevo, asígnelo a una nueva variable:
two_facts = fact + "No sound can be heard on the Moon."
print(two_facts)

# Una recomendación es usar comillas triples """Hello World""" para evitar errores al usar comillas dobles o simple en una oración.
# Además con el uso de comillas triples puede lograr saltos de línea, por ejemplo:
multiline = """Facts about the Moon:
There is no atmosphere.
There is no sound."""
print(multiline)