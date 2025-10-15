# # Funções

# def saudacao():  #definindo a função
#     print('hello world')

# saudacao()  # chamando a função

def linha():
    print(30*"=")


def saudacao(n):
    print(f'Óla, {n}. Seja bem vindo.')


def soma_numeros(n1,n2):
    resultado = n1 + n2
    print(resultado)


# nome = input('Qual o seu nome ? ')

# linha()
# saudacao(nome)
# soma_numeros(1,2)

for n in range(3):
    n1 =float(input("Digite o primero número: "))
    n2 =float(input("Digite o primero número: "))
    soma_numeros(n1,n2)
