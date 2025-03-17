import pandas as pd

dadosProdutos = pd.read_csv('tabelas3.csv')

indice = dadosProdutos['PRECO'].idxmax()
#obtendo o produto com maior preco
produto_maior_preco = dadosProdutos.loc[indice,'PRODUTO']

preco = dadosProdutos.loc[indice,'PRECO']

print('Produto Com Maior quantidade:', produto_maior_preco,'com', preco,'unidade')