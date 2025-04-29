# Importar bibliotecas necessárias
import pandas as pd
import numpy as np

# Etapa 2: Carregar os dados e visualizar as primeiras linhas
diabetes_data = pd.read_csv('diabetes.csv')
print("Primeiras linhas dos dados:")
print(diabetes_data.head())

# Etapa 3: Contar o número de colunas e linhas
print(f'Número de colunas: {diabetes_data.shape[1]}')
print(f'Número de linhas: {diabetes_data.shape[0]}')

# Etapa 5: Verificar valores nulos nas colunas
print("\nValores nulos por coluna:")
print(diabetes_data.isnull().sum())

# Etapa 6: Calcular estatísticas descritivas
print("\nEstatísticas descritivas dos dados:")
print(diabetes_data.describe())

# Etapa 7: Análise das colunas com valores anômalos (0)
# Identificar colunas relevantes e verificar se algum valor é 0
print("\nValores mínimos e máximos para identificar anomalias:")
print(diabetes_data[['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']].min())
print(diabetes_data[['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']].max())

# Etapa 9: Substituir valores 0 por NaN nas colunas relevantes
diabetes_data[['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']] = \
    diabetes_data[['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']].replace(0, np.nan)

# Etapa 10: Verificar valores nulos novamente após substituição
print("\nValores nulos após substituição de 0 por NaN:")
print(diabetes_data.isnull().sum())

# Etapa 11: Imprimir linhas com valores nulos
print("\nLinhas com valores nulos:")
print(diabetes_data[diabetes_data.isnull().any(axis=1)])

# Etapa 13: Verificar os tipos de dados das colunas
print("\nTipos de dados das colunas:")
print(diabetes_data.dtypes)

# Etapa 14: Explorar os valores únicos na coluna 'Outcome'
print("\nValores únicos na coluna 'Outcome':")
print(diabetes_data['Outcome'].unique())

# Etapa 15: Corrigir tipo de dado da coluna 'Outcome' se necessário
# Caso a coluna 'Outcome' esteja como tipo 'object', converta para 'int'
if diabetes_data['Outcome'].dtype == 'object':
    diabetes_data['Outcome'] = diabetes_data['Outcome'].astype(int)

print("\nTipos de dados após conversão da coluna 'Outcome':")
print(diabetes_data.dtypes)

# Etapa 16: Estender o projeto (Exploração adicional)
# Usar value_counts para explorar a distribuição de valores nas colunas
print("\nDistribuição de valores em 'Outcome':")
print(diabetes_data['Outcome'].value_counts())

# Fim do código
