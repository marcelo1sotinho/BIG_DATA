# lista - Estrutura Mútavel

frutas =["maçã", 'banana', 'laranja']
print(frutas)  # lista completa
print(frutas[2])  #terceiro da lista
print(frutas[-1])  #último da lista
print(frutas[1:])  # a partir do segundo elemento

frutas.append('uva')
print(frutas)

frutas[1] = 'mamão' # altera o elemnto da segunda posição
print(frutas)

frutas.remove("laranja")
print(frutas)

# Usando for com a lista
c = 1
for item in frutas:
    print(f'{c}- {item}')
    c += 1  #c = c + 1
    c = c + 1









