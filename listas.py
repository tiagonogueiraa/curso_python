frutas = ["laranja", "maca", "uva"]
print(frutas)

frutas = []
print(frutas)

letras = list("python")
print(letras)

numeros = list(range(10))
print(numeros)

carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]
print(carro)
# indice positivo
print(carro[5])
# indice negativo
print(carro[-2])

# MATRIZ 
matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

print(matriz[0])  # [1, "a", 2]
print(matriz[0][0])  # 1
print(matriz[0][-1])  # 2
print(matriz[-1][-1])  # "c"

#  a partir da posicao 2
print(carro[2:])

print(carro[:2])

carros = ["Gol", "Polo", "F-pace", "Onix"]

for v in carros:
    print(v)

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

# Filtrar lista
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)

# Modificar valores
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero**2 for numero in numeros]
print(quadrado)

arrayQ = []
for numero in numeros:
    arrayQ.append(numero ** 2)

print(arrayQ)

# Copy
lista = [1, "Python", [40, 30, 20]]

l2 = lista.copy()

print(lista)  # [1, "Python", [40, 30, 20]]

print(l2)

print(f"Lista 2: {id(l2)}, Lista 1:{id(lista)}")

qtdItem = lista.count('Python')
print(qtdItem)

# extends
# para juntar listas
# obs ele nn faz merge, ele apenas junta
linguagens = ["python", "js", "c"]

print(linguagens)  # ["python", "js", "c"]

linguagens.extend(["java", "csharp"])

print(linguagens)  # ["python", "js", "c", "java", "csharp", "java"]

print(linguagens.index("java"))  # 3
print(linguagens.index("python"))  # 0

linguagens = ["python", "js", "c", "java", "csharp", "PHP"]

# pop - remove do array
print(linguagens)
print(linguagens.pop())  # csharp
print(linguagens.pop())  # java
print(linguagens.pop())  # c
print(linguagens.pop(0))  # python

print(linguagens)

linguagens.remove("js")

print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp", "php"]

# sort

linguagens.sort()
print(linguagens)

linguagens.sort(reverse=True)
print(linguagens)

# palavras em ordem crescente
# lambda é uma função anonima
# para cada item ele executa len(x) - tamanho de x
linguagens.sort(key=lambda x: len(x))

print(linguagens)
linguagens.sort(key=lambda x: len(x), reverse=True)

print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]

# a diferenca do sort é que o sorted é uma função
print(sorted(linguagens, key=lambda x: len(x)))  # ["c", "js", "java", "python", "csharp"]
print(sorted(linguagens, key=lambda x: len(x), reverse=True))  # ["python", "csharp", "java", "js", "c"]

print([n**2 if n > 6 else n for n in range(10) if n % 2 == 0])