texto = input("Informe um texto: ")
VOGAIS = "AEIOU"


# Exemplo utilizando um iterável
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print()  # adiciona uma quebra de linha


# Exemplo utilizando a função built-in range
for numero in range(0, 51, 5):
    print(numero, end="\n")

# OPCAO 1 DE WHILE
# opcao = -1

# while opcao != 0:
#     opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

#     if opcao == 1:
#         print("Sacando...")
#     elif opcao == 2:
#         print("Exibindo o extrato...")
# else:
#     print("Obrigado por usar nosso sistema bancário, até logo!")


# OPCAO 2 WHILE

while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break

    if numero % 2 == 0:
        continue

    print(numero)