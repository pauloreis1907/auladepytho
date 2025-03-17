produto = {
    'nome':['feijao','Arroz','Farinha'],
    'quantidade':[ 10,10,100],
    'preco':[15,10,5]
}

for nome, quantidade, preco in zip(produto['nome'], produto['quantidade'], produto['preco']):
    print(f'nome:{nome}, Quantidade:{quantidade}, preco:{preco}')