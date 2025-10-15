import random
import os


def numeros_aletorios(i,f,qtd):
    return [random.randint(i,f) for num in range(qtd)]

os.system('cls')

# Gerar números. Usuário Escolhe inicio, fim e a qtd
inicio = int(input('Infome o inicio: '))
fim = int(input('Infome o final: '))
quantidade = int(input('Quantos números ? '))

print(inicio, fim, quantidade)

numeros = numeros_aletorios(inicio, fim, quantidade)
print(numeros)