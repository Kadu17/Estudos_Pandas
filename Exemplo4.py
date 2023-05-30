import pandas as pd
arq = pd.read_excel('professores.xlsx')
tam = len(arq)
print(tam)
arq['idade'] = 'idade'
for i in range(0, tam):
    j = arq.loc[i, 'nome']
    k = int(input(f'Idade de {j} '))
    arq.loc[i, 'idade'] = k

print(arq)
