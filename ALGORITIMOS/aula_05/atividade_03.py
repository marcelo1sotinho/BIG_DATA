for n in range(10):
    n1 = float(input("Infome a primeira nota "))
    n2 = float(input("Infome a segunda nota "))
    n3 = float(input("Infome a terceira nota "))
    n4 = float(input("Infome a quarta nota "))
    
    media = (n1 + n2 + n3 + n4) / 4
    if media >= 7:
        print("aprovado")
    elif  5 <= media < 7:
        print("recuperação")
    elif media < 5:
        print("reprovado")



