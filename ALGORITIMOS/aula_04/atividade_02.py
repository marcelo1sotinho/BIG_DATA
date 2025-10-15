valor = float(input("Qual é o valor da compra ? "))
pagamento = (input("A forma de pagemento é á vista ? ")).upper()


if valor > 250 and pagamento == "SIM":
    total = valor - (valor *( 16 /100))
    print(total)
else:
    print(valor)
