import pandas as pd
import matplotlib.pyplot as plt

dadosProdutos = pd.read_csv('tabeladecultivo.csv', delimiter=',')
print(dadosProdutos['Cultivo'])
print(dadosProdutos['Produtividade'])

#chamando o grafico em pizza 
labels = dadosProdutos['Cultivo']
sizes = dadosProdutos['Produtividade']

figl,axl = plt.subplots()

axl.pie(sizes,labels=labels,autopct='%1.1f%%', shadow= True, startangle=90)

axl.axis('equal')

plt.title('gravico do PRocutos')

plt.show()