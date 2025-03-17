import pandas as pd
import matplotlib.pyplot as plt
#carregando os dados
dadosProdutos = pd.read_csv('tabelas3.csv', delimiter=',')
#criando o grafico por ano para cada produto
plt.figure(figsize=(10, 6))
#plantando os dados para cada produto
for produto in dadosProdutos['PRODUTO'].unique():
    dadosProduto = dadosProdutos[dadosProdutos['PRODUTO'] == produto]
    plt.plot(dadosProduto['ANO'],dadosProduto['PRECO'], label=produto, marker='o')

#adicinamdo titulo e rotulos
plt.title('Preço dos Produtos ao longo do ano:')
plt.xlabel('ANO')
plt.ylabel('PRECO')
plt.legend(title='PRODUTO')
#exibindo o grafico
plt.grid(True)
plt.show()

#