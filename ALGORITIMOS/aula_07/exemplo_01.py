# i = int(input('Quer contar a partir de quanto: '))
# f = int(input('Contar até quanto: '))


# while i < f :
#     print(f'{i+1} HELLO WORLD')
#     i = i + 1 # i += 1 var recebe o que já tinha em 1 somando + 1
#     i += 1


# print('Saiu do loop')
# print(f'O valor de N é {i}')


# soma = 0.0
# continuar = 'S'

# while continuar == 'S':
#     numero = float(input('Informe o numero: '))
#     soma = soma + numero

#     continuar = input('Quer continuar ? (S/N) ')[0].upper()
#     print(f'Você escolheu {continuar}')

# print(f'o resultado da soma é {soma}')

# notas = []
# continuar = 'S'

# while continuar == 'S':
#     nota = float(input('Informe nota do aluno: '))
#     notas.append(nota)

#     continuar = input('Quer continuar ? (S/N) ')[0].upper()

# media = sum(notas) / len(notas)
# print (f'\nNotas digitadas {notas}')
# print(f'A média foi {media}')


pessoas = []
continuar = "S"

while continuar.upper() == 'S':
    nome = input('Digite o nome: ')
    idade = int(input(f'Digite a idade de {nome}: '))

    pessoa = {
        "Nome": nome,
        "Idade": idade
    }
    
    pessoas.append(pessoa)

    continuar = input('Quer continuar ? (S/N) ')[0]

# print('\n##### Pessoas cadastras #####')
# print(pessoas)

for p in pessoas:
    print(f'Nome: {p["Nome"]}, Idade: {p["Idade"]}')






