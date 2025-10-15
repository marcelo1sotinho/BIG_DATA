# Biblioteca para gerar números aleátorios
# As bliliotecas são importadas pelo comando import

import random

def calculo(a,b):
    multiplicacao = a * b
    return multiplicacao


# exemplo 01
n = random.randint(1,10)
m = random.randint(1,10)

# print(n,m)
# print(n+m)


multiplicacao = calculo(n,m)
print(multiplicacao)

