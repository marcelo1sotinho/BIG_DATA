import random
import os

n = random.randint(1, 10)
m = random.randint(1, 10)

print(n, m)
os.system('cls')

# exemplos 02
# Gerar  uma lista de números aleatórios
lista_numeros = [random.randint(1,10) for num in range(5)]
print(lista_numeros)

for num in range(5):
    x = random.randint(1,10)
    lista_numeros.append(x)