print("Hello World!")
print("ola aaa")

# conta - tipos de dados int(), float(), str(), bool()

print(11 + 10 + 1000)

print(1.5 + 1 + 0.5)

print(True)

print(False)

nome = "Tiago"

idade = 28

print(nome, idade)

nome, idade = "Tiago", 30

print(nome, idade)

limite_saque_diario = 1000

# constante
# USANDO SNACK CASES COM O _ (UNDERLINE) porém ele permite alterar o dado usando a msm variável
BRAZILIAN_STATES = ["SP", "RJ", "SC", "RS"]

print(BRAZILIAN_STATES)

preco = 10
print(preco)

print(preco / 2)
# vira um numero float com uma barra

print(preco // 2)
# vira um numero inteiro com duas barras

preco = "10.50"
idade = "28"
print("valor bool")
print(bool(preco))

print(int(idade))

print(type(idade))


saldo = 1000
saque = 200
limite = 100
print('AND')
print(saldo >= saque and saque <= limite)
print('OR')
print(saldo >= saque or saque <= limite)


print("NOT")
not 1000 > 1500

contatos_emergencia = []
not contatos_emergencia

print("IS")

curso = "Curso de Python"
nome_curso = curso

# valida msm regi�o de mem�ria? 

print(curso is nome_curso) #retorna true
print(curso is not nome_curso) #retorna false


frutas = ["limão", "uva"]

print("laranja" in frutas)
print("laranja" not in frutas)


def sacar(self, valor:float) :
    if self.saldo > valor:
        self.saldo -= valor


def sacarTeste(valor) :
    saldo = 500

    if saldo > valor:
        saldo -= valor
        a = 'Saldo --->>> ' + str(saldo)
        print("----------- SAQUE REALIZADO --------------")
        print(a)
    

print(sacarTeste(133.33))

