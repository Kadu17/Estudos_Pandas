import pandas as pd

arquivo = pd.ExcelFile('professores.xlsx')
df = pd.read_excel(arquivo, 'Sheet1')
nomes = df[['nome', 'formacao']]
print(nomes.loc[2])