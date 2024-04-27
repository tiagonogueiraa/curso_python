# SET NEM SEMPRE TRAZ ORDENADO

numeros = set([1, 2, 3, 1, 3, 4])
print(numeros)  # {1, 2, 3, 4}

letras = set("abacaxi")
print(letras)  # {"b", "a", "c", "x", "i"}

carros = set(("palio", "gol", "celta", "palio"))
print(carros)  # {"gol", "celta", "palio"}

# para acessar o valor terá que converter em lista

carros.add("Fusca")
print(carros)

#limpar o set
# carros.clear()

# carros.copy() copia

# carros.remove("gol") - remove dá erro se o elemento nn existir e o discard não 

carros.discard("Fusca")

print(carros)

print("gol em carros?")
print("gol" in carros)

letras = list(letras)

print(letras[0])

for val in carros:
    print(val)

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

resultado = conjunto_a.intersection(conjunto_b)
print(resultado)

resultado = conjunto_a.difference(conjunto_b)
print(resultado)

resultado = conjunto_b.difference(conjunto_a)
print(resultado)

resultado = conjunto_a.union(conjunto_b)
print(resultado)


# conjunto a está no conjuto b?
resultado = conjunto_a.issubset(conjunto_b)  # True
print(resultado)

resultado = conjunto_b.issubset(conjunto_a)  # False
print(resultado)

# isdisjoint
# todos os elementos não estão presentes no conjunto
conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

resultado = conjunto_a.isdisjoint(conjunto_b)  # True
print(resultado)

resultado = conjunto_a.isdisjoint(conjunto_c)  # False
print(resultado)