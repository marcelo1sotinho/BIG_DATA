from InquirerPy import prompt

codigo = [
    {
    "type": "list",
    "message": "Infome o código:",
    "choices": ["codigo 1", "codigo 2", "codigo 3", "codigo 4", "codigo 5", "codigo 6", "codigo 7", "codigo 8", "codigo 9", "codigo 10", "codigo 11"]
    }
    
]

resultado = prompt(codigo)

match resultado:
    case "codigo 1":
        print("Sul")
    case "codigo 2":
        print("Norte")
    case "codigo 3":
        print("Leste")
    case "codigo 4":
        print("Oeste")
    case "codigo 5":
        print("Nordeste")
    case "codigo 6":
        print("Nordeste")
    case "codigo 7":
        print("Sudeste")
    case "codigo 8":
        print("Sudeste")
    case "codigo 9":
        print("Sudeste")
    case "codigo 10":
        print("Centro-Oeste")
    case "codigo 1":
        print("Noroeste")

# codigo = float(input("Informe o código: "))

# match codigo:
#     case 1:
#         print("c")
#     case 2:
#         print("Norte")
#     case 3:
#         print("leste")
#     case 4:
#         print("Oeste")
#     case 5 |6:
#         print("Nordeste")
#     case n if 7 <= n <= 9:
#         print("Sudeste")
#     case 10:
#         print("Centro-Oeste")
#     case 11:
#         print("Noroeste")
#     case _:
#         print('Código Inválido')
    

    
    