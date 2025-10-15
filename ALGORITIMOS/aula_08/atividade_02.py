# Crie uma função que calcule o dobro, o triplo e ao quadrado

def calcular(num):
    dobro = num * 2
    triplo = num * 3
    quadrado = num * num
    print(f'O dobro do número é {dobro}, o triplo é {triplo} e o quadrado é {quadrado}')


num = float(input('Informe um número: '))

calcular(num)

