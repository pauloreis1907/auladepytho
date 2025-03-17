import pandas as pd
import matplotlib.pyplot as plt

dadosProdutos = pd.read_csv('tabeladecultivo.csv', delimiter=',')

indice = dadosProdutos['Produtividade'].idxmax()
indice2 = dadosProdutos['Produtividade'].idxmin()
#obtendo o produto com maior preco
produto_maior_preco = dadosProdutos.loc[indice,'Cultivo']
produto_menor_preco = dadosProdutos.loc[indice2,'Cultivo']

p = dadosProdutos.loc[indice,'Produtividade']
p2 = dadosProdutos.loc[indice2,'uso_agua']
print(dadosProdutos)

print('\nProduto Com Maior Produtividade:', produto_maior_preco,'com', p,'g','PRODUTIVIDADE')
print('\nProduto Com Menor usor de agua:', produto_menor_preco,'com', p2,'L','Uso de agua')
#apresetando grafico

labels = dadosProdutos['Cultivo']
sizes = dadosProdutos['Produtividade']

figl,axl = plt.subplots()

axl.pie(sizes,labels=labels,autopct='%1.1f%%', shadow= True, startangle=90)

axl.axis('equal')

plt.title('grafiico do Produtos')

plt.show()

plt.figure(figsize=(10, 6))

for produto in dadosProdutos['Cultivo'].unique():
    dadosProduto = dadosProdutos[dadosProdutos['Cultivo'] == produto]
    plt.plot(dadosProduto['Produtividade'],dadosProduto['Ano'], label=produto, marker='o')

plt.title('Preço dos Produtos ao longo do ano:')

#plt.ylabel('Cultivo')
#plt.ylabel('Produtividade')
#plt.ylabel('uso_agua')
plt.xlabel('P')
plt.ylabel('A')
plt.legend(title='Cultivo')

plt.grid(True)
plt.show()
