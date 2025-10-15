# anote todos os produtos e os pesos

import os

c = 0

produtos = []
pesos = []

while True:
    
    print('\nMENU')
    print('1 - Resgistrar produto')
    print('2 - Resumo dos produtos')
    print('3 - FIM')
    opcao = input('Escolha uma opção: ')



    if opcao == '1':
         produto = input(f'Informe o produto {c + 1}: ')
         peso = float(input('Informe o peso: '))
         c +=1

         produtos.append(produto)
         pesos.append(peso)

    elif opcao == '2':
         total_peso = sum(pesos)

         print('====== Resumo dos produtos ======')

         for peso, produto in zip(pesos, produtos):
            print(f'\nO produto é {produto}')
            print(f'O peso é {peso}Kg ')
         
         print(f'\nO total do peso é {total_peso}')

    elif opcao == '3':
        break
    else:
        print('Opção Inválida')
    









