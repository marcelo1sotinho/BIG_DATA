
precos = []
c = 0

while True:
    resposta = input(f'Informe o preço do produto {c + 1}: ')

    if resposta.upper() == 'SAIR':
        print('\n============ Resumo da Compra ============' )
        print(f'Preços dos produtos {precos}')
        print(f'Valor Total: {total:.2f}')
        break
    
    preco = float(resposta)
    precos.append(preco)
    precos.sort()

    total = sum(precos)
    
    print(f'Preço: {preco}')
    print(f'Valores: {precos}')
    c += 1

  
