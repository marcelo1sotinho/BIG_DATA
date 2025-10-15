num = int(input('Informe um número de 0 a 8: '))

c = 1
espaco = num - 1

for i in range(num):
    print(f'{" " * espaco}{"#" * c}  {"#" * c}')

    c += 1
    espaco -= 1
