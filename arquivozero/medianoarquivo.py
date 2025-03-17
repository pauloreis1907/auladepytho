import pandas as pd

dadosProdutos = pd.read_csv('tabelas2.csv')
print(dadosProdutos.columns)
dadosProdutos['PRECO'].max()
print('Media de Preços dos Produtos', dadosProdutos['PRECO'].mean())