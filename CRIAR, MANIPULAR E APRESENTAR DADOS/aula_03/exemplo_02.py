# Quartis
# Divide o conjuto de dados em 4 partes percentuais iguais
# Método muito utilizado em análise de dados com estatística descritiva

import numpy as np 

#exemplo
idade = [35, 25, 38, 32, 45, 42, 36, 29, 40 ,32 ]
print(idade)

array_idade = np.array(idade)
print(array_idade)

q1 = np.quantile(array_idade, 0.25)
q2 = np.quantile(array_idade, 0.50)
q3 = np.quantile(array_idade, 0.75)

print(f'\nQ1: {q1}')
print(f'Q2: {q2}')
print(f'Q3: {q3}')