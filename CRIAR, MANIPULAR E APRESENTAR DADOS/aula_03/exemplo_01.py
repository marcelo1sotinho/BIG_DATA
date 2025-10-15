import numpy as np 

dados_salario = [2000, 2500, 3500, 3000, 4000, 30000]

#vCalcula Média com numpy
media = np.mean(dados_salario)

# Calcula Médiana
# A mediana é o valor que está representando no centro da distribuição dos dados
# Quando a qtd de valores for PAR, somamos e dividimos por 2, os dois valores que estão mais ao centro da distribuição
mediana = np.median(dados_salario)

print(f"Média: {media}")
print(f"Médiana: {mediana}")
