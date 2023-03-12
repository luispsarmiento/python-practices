# Formato con sigo de porcentaje (%)
mass_percentage = "1/6"
print("On the Moon, you would weigh about %s of your weight on Earth" % mass_percentage)

# Formato con el método format()
print("On the Moon, you would weigh about {} of your weight on Earth".format(mass_percentage))
print("""You are lighter on the {0}, because on the {0} you would weigh about {1} of your weight on Earth""".format("Moon", mass_percentage))
print("""You are lighter on the {moon}, because on the {moon} you would weigh about {mass} of your weight on Earth""".format(moon="Moon", mass=mass_percentage))

# f-strings, este permite interpolar variables y expresiones entre llaves, por ejemplo:
print(f"On the Moon, you would weigh about {mass_percentage} of your weight on Earth")
print(f"On the Moon, you would weigh about {round(100/6, 1)}% of your weight on Earth")