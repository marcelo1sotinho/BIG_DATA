import os


def multa(a):
       resultado = (a - 100) * 4
       return resultado
   
os.system('cls')


peixe = float(input('Informe o peso do peixe: '))

if peixe > 100:
    resulatdo = multa(peixe)
    print(f'Total da multa {resulatdo}')
else:
    print('Não há multa')