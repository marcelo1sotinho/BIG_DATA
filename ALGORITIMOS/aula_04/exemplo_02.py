idade = int(input('Informe a idade: '))
acompanhante = input('Acompanhate ? ').upper()

if idade >= 16 or acompanhante == "SIM":
    print('Liberado')
else:
    print ('Você não pode entrar')