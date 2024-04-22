nome = "gUIlherME"

print(nome.upper())
print(nome.lower())
# primeira em maiscula
print(nome.title())

texto = "  Olá mundo!    "

print(texto)
print(texto + ".")
print(texto.strip() + ".")
print(texto.rstrip() + ".")
print(texto.lstrip() + ".")

menu = "Python"
# centraliza com espaco em branco mas se tiver segundo parâmetro coloca ele no lugar de espaço em branco
print("####" + menu + "####")
print(menu.center(14))
print(menu.center(14, "#"))
print("-".join(menu))

# INTERPOLAÇÃO DE VARIÁVEIS

nome = "Tiago"
idade = 28
profissao = "Programador"
linguagem = "Python"

print("Olá, me chamo %s Eu tenho %d anos de idade, tablho como %s e estou matriculado no curso de %s. " % (nome, idade, profissao, linguagem))

# HOJE USA O MÉTODO FORMAT
# é possível colocar o índice da posição dentro da chave {1}, se colocar 1 sempre iria pegar a variável idade
print("Olá, me chamo {} Eu tenho {} anos de idade, tablho como {} e estou matriculado no curso de {}. ". format(nome, idade, profissao, linguagem))

print("Olá, me chamo {nome} Eu tenho {idade} anos de idade, tablho como {profissao} e estou matriculado no curso de {linguagem}. ". format(nome=nome, idade = idade, profissao = profissao, linguagem = linguagem))

# COM OPÇÃO f-string
print(f"Olá, me chamo {nome} Eu tenho {idade} anos de idade, tablho como {profissao} e estou matriculado no curso de {linguagem}. ")

saldo = 10.45689
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.1f}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.1f}")


# FATIAMENTO CORTAR STRING 

nome = "Tiago de Souza Nogueira"

print(nome[0])


print(nome[:9])

print(nome[:10])

print(nome[10:16])

print(nome[10:16:2])

print(nome[:]) # pega td
print(nome[::-1]) # espelhamento da string


# STRING MULTIPLAS LINHAS
# interpolacao f string (f""")

mensagem = f"""
Olá meu nome é {nome},
Eu estou aprendendo python
"""

print(mensagem)


print(
    """
    ============= MENU =============

    1 - Depositar
    2 - Sacar
    0 - Sair

    ================================

            Obrigado por usar nosso sistema!!!!
"""
)