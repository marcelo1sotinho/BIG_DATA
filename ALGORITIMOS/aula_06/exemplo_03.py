# Dicionario 
# É uma coleções de pares Chaves e Valor.
# Usado quando queremos associar um chave única a um valor.
#Exemplo: Cadastro de Alunos e suas notas, Cadastro de Funcionarios.

# [] Listas
# () Tuplas
# {} Dicionário

# Cadastro

aluno ={
    "Nome": 'Pedro',
    'Idade': 17,
    'Curso': 'Informática'
}

print(aluno)  #Imprimindo todos o elementos

print(aluno['Nome'])  # Imprindo a chave nome
print(aluno['Curso'])  #Imprimindo a chave curso

aluno['Média'] = 7.9  #Adiciona chave valor
print(aluno)

aluno['Curso'] = 'Inglês' # Altera valor da chave
print(aluno)

del aluno ['Idade']
print(aluno)


# Usando for no dicionario

# for c, v in aluno.items():
#     print(f'Chave: {c} | Valor: {v}')

for v in aluno.values(): # aluno.keys() para as chaves
    print(f'Valor: {v}')

