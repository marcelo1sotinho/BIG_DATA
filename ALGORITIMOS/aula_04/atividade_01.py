valor = float(input("Qual é o valor da compra ? "))

if valor > 250:
    total = valor - (valor *( 16 /100))
    print(total)
else:
    print(valor)





