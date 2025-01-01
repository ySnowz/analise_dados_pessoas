# Importando a biblioteca pandas para manipulação de dados
import pandas as pd

# Dicionário contendo dados de 20 pessoas, com nome, idade e cidade
dados = {
    'Nome': [
        'João', 'Maria', 'Pedro', 'Ana', 'Carlos', 'Fernanda', 'Ricardo', 'Juliana', 
        'Lucas', 'Patrícia', 'Marcos', 'Camila', 'Rafael', 'Isabela', 'Gustavo', 
        'Larissa', 'Bruno', 'Mariana', 'Diego', 'Tatiane'
    ],
    'Idade': [
        25, 30, 35, 28, 40, 22, 33, 27, 29, 31, 26, 24, 32, 23, 34, 21, 36, 20, 37, 38
    ],
    'Cidade': [
        'São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba', 'Porto Alegre', 
        'Salvador', 'Fortaleza', 'Recife', 'Manaus', 'Belém', 'Goiânia', 'Florianópolis', 
        'Vitória', 'Natal', 'Campo Grande', 'Cuiabá', 'João Pessoa', 'Teresina', 'Aracaju', 'Maceió'
    ]
}

# Criando uma série (Series) do pandas com as idades, usando os nomes como índice
serie_idades = pd.Series(dados['Idade'], index=dados['Nome'])

# Criando um DataFrame do pandas a partir do dicionário de dados
df_idades = pd.DataFrame(dados)

# Exibindo a série de idades
print(f'Idades: \n{serie_idades}\n')

# Calculando e exibindo a média das idades
print(f'Média de idades: {serie_idades.mean()}')

# Exibindo a maior idade
print(f'Maior idade: {serie_idades.max()}')

# Exibindo a menor idade
print(f'Menor idade: {serie_idades.min()}')

# Exibindo a soma das idades
print(f'Soma das idades: {serie_idades.sum()}')

# Exibindo a quantidade de idades na série
print(f'Quantidade de idades: {serie_idades.count()}\n')

# Exibindo uma descrição estatística da série (média, desvio padrão, mínimo, máximo, etc.)
print(f'Descrição: \n{serie_idades.describe()}\n')

# Exibindo os valores únicos presentes na série de idades
print(f'Valores únicos: \n{serie_idades.unique()}\n')

# Exibindo a contagem de cada valor único na série de idades
print(f'Contagem de valores: \n{serie_idades.value_counts()}\n')

# Exibindo as primeiras 5 linhas do DataFrame
print('Primeiras 5 linhas do DataFrame: \n')
print(df_idades.head())