# Tratando erros - Estrutura try Excpetion / else / finally

contador = 1
resultado = 0
while contador <= 3:
    try:
        n1 = float(input("Número: "))
        n2 = float(input("Número: "))
        
        resultado = n1 / n2
        
    
    except ZeroDivisionError:
        print('Não há divisão por 0')
    
    except (ValueError, TypeError):
        print('Iforme somente números')
        
    print(resultado)
    contador += 1

    ########################################

contador = 1
resultado = 0
while contador <= 3:
    try:
        n1 = float(input("Número: "))
        n2 = float(input("Número: "))
        
        resultado = n1 / n2
        
    
    except ZeroDivisionError:
        print('Não há divisão por 0')
    
    except (ValueError, TypeError):
        print('Iforme somente números')
    
    else:   
        print(resultado)
        contador += 1 

    finally:
        print('Operação finalizada')