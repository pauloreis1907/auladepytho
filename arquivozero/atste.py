import pandas as pd
import matplotlib.pyplot as plt
cor = ['#0000FF','pink','#00FFFF','#A52A2A','#5F9EA0','#F0F8FF']

dadosProdutos = pd.read_csv('pppp.csv', delimiter=';')
print(dadosProdutos)
#print(dadosProdutos['Value'])

#chamando o grafico em pizza 
labels = dadosProdutos['item']
sizes = dadosProdutos['Value']


figl,axl = plt.subplots()

axl.pie(sizes,labels=labels,autopct='%1.1f%%', shadow= True, startangle=90,colors = cor)

axl.axis('equal')

plt.title('Grafico Populução dos pais de 2022 e 2023\n')

plt.show()

