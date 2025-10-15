from InquirerPy import prompt

c = 0

produtos = []
pesos = []

while True:

    pergunta = [
        {
            'type': 'list',
            'message': 'Escolha uma opção: ',
            'choices': ['Resgistrar produto','Resumo dos produtos','FIM']

        }
    ]

    resposta = prompt(pergunta)

    opcao = list(resposta.values())[0]

 

    if opcao == 'Resgistrar produto':
         produto = input(f'Informe o produto {c + 1}: ')
         peso = float(input('Informe o peso: '))
         c +=1

         produtos.append(produto)
         pesos.append(peso)

    elif opcao == 'Resumo dos produtos':
         total_peso = sum(pesos)

         print('====== Resumo dos produtos ======')

         for peso, produto in zip(pesos, produtos):
            print(f'\nO produto é {produto}')
            print(f'O peso é {peso}Kg ')
         
         print(f'\nO total do peso é {total_peso}')

    elif opcao == 'FIM':
        break
    else:
        print('Opção Inválida')
    