resultados = []

for v in range(5):
    print(f'Vendedor {v+1}')

    venda1 = float(input(f'Informe o válor da venda {v+1}: '))
    venda2 = float(input(f'Informe o válor da venda {v+1}: '))
    venda3 = float(input(f'Informe o válor da venda {v+1}: '))
    venda4 = float(input(f'Informe o válor da venda {v+1}: '))
   
    media = (venda1 + venda2 + venda3+ venda4) / 4

    resultados.append(media)

    if media >= 1000:
        print('Bom!!!')
    elif media >= 500:
        print("Pode Melhorar")
    else:
        print('Não atingiu a meta')

print(f'As médias são {resultados}')

