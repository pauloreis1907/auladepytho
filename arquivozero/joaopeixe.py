import pandas as pd
import matplotlib.pyplot as plt

dadosProdutos = pd.read_csv('joao.csv', delimiter=',')

indice = dadosProdutos['produtividade'].idxmax()
indice2 = dadosProdutos['produtividade'].idxmin()
#obtendo o produto com maior preco
produto_maior_preco = dadosProdutos.loc[indice,'cultivo']   
produto_menor_preco = dadosProdutos.loc[indice2,'cultivo']

print(dadosProdutos)


p = dadosProdutos.loc[indice,'produtividade']
p2 = dadosProdutos.loc[indice2,'vendas']


print('\nProduto Com Maior Produtividade:',produto_maior_preco,'com', p,'g','PRODUTIVIDADE')
print('\nProduto Com Menor Indice vendas:', produto_menor_preco,'com', p2,'Vendas')
#apresetando grafico


labels = dadosProdutos['cultivo']
sizes = dadosProdutos['vendas']

figl,axl = plt.subplots()

axl.pie(sizes,labels=labels,autopct='%1.1f%%', shadow= True, startangle=90)

axl.axis('equal')

plt.title('Grafiico do Produtos\n')

plt.show()

# produvidade , divido por custo medio