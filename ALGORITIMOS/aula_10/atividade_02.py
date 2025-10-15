import os 

def multa(a):
       resultado = (a - 100) * 4
       return resultado


os.system('cls')

peixes = []
continuar = "sim"

while continuar == 'sim':
    peixe = float(input('Informe o peso do peixe: '))
    peixes.append(peixe)
    continuar = input('Deseja continuar ? ')

for n in peixes:
    if n > 100:
        r = multa(n)
        print(f'Total da multa para {n}Kg é {r}$')
    else:
        print(f'Não há multa para {n}Kg')

