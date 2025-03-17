arquivo = open('contato.txt','r')

for linha in arquivo:
    print(linha)
arquivo.close()

arquivo = open('contato.txt','a')
arquivo.write('\n JOSE')
arquivo.close()