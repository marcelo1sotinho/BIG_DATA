# # MATCH CASE

# print(
#     '''
#     1 - Hamburguer
#     2 - Pizza
#     3-  Salada
#     ''' 
# )

# # opcao = input('Escolha um lanche: ')

# # match opcao:
# #     case "1":
# #         print('Hamburguer ')
# #     case "2":
# #         print('Pizza')
# #     case "3":
# #         print('Salada')
# #     case _:
# #             print('Opção inválida')


# # Exemplo 2 

nota = float(input('informe a nota: '))

match nota:
    case 1 | 2 | 3: # n if 1 <= n  <= 3:
        print('desempemho muito baixo')
    case 4 | 5 | 6:
        print('Razoável')
    case 7:
        print('Bom')
    case n if 8 <= n <= 10:
        print('Excelente') 
    case _:
        print('Nota inválida')
    