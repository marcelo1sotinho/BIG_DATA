# While True

c = 0
while True:
    print(f'Estou no while{c + 1}...')
    res = (input('Digite um número: '))

    if res.upper() == 'SAIR':
         break
    
    c = c + 1


    
        