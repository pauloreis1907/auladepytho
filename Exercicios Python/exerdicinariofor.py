produto = {
    'nome':['feijao','Arroz','Farinha'],
    'quantidade':[ 10,10,100]
}
#chama os items , e lista, zip : juntas dois elementos
for nome, quantidade in zip(produto['nome'],produto['quantidade']):
    
    print("nome:",nome)
    print('quantidade:',quantidade)