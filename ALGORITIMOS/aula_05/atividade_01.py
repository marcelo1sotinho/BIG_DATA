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

# Match case

# n1 = float(input("Infome a primeira nota "))
# n2 = float(input("Infome a segunda nota "))
# n3 = float(input("Infome a terceira nota "))
# n4 = float(input("Infome a quarta nota "))

# media = (n1 + n2 + n3 + n4) / 4

# match media:
#     case m if m > 7:
#         print("aprovado")
#     case m if 5 <= m <= 7:
#         print(" recuperção")
#     case m if m < 5:
#         print("reprovado")

