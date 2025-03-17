import pandas as pd

dadosProdutos = pd.read_csv('produtos.csv')
dadosProdutos{'preco'}.max()
print('Media de Preços dos Produtos', dadosProdutos{'preco'}.max())