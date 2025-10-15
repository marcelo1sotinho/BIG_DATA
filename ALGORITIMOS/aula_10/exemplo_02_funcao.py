def calcula_preco( a, b):
    return a * b


def calcula_desconto(a):
    if a >= 100:
        desc = a - (a *10/100)
        return desc
        # return a * 0.9


# Programa principal
preco = float(input('Preço: '))
qtd = int(input('Quantidade: '))

valor = calcula_preco(preco, qtd)

valor_final = calcula_desconto(valor)

print(f'Valor sem desconto: {valor:.2f}')
print(f'Valor com desconto: {valor_final:.2f}')