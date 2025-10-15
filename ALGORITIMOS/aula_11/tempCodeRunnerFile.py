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

    opcao = prompt(pergunta)
    print(opcao)
   