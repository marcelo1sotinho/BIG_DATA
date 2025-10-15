saldo = 500.0
print(f'Seu saldo atual é {saldo}')

try:
    valor = float(input('Quanto você deseja sacar ? '))

except Exception as e:
    print(f'Algo deu errado{e} ')

else:
    if valor <= 0:
        print('O valor não pode ser negativo')
    elif valor > saldo:
        print('Saldo insuficiente')
    else:
        saldo -= valor
        print('Saque realizado com sucesso')
        print(f'Saldo restante {saldo:.2f}')
finally:
    print('Operação finalizada')