with open('texto.txt','w', encoding='utf-8') as file:
    for i in range(3):
        frase = input(f'digite{i+1}ª frase:')
        file.write(frase+'\n')

print('FRASES SALVAS COM SUCESSO!')

def contavagais(texto):
    vogais = 'aeiouAEIOU'
    contagem =  0
    for vogal in texto:
        if vogal in vogais:
            contagem+=1
    return contagem
with open('texto.txt','r', encoding='utf-8') as file:
    conteudo = file.read()
totalV = contavagais(conteudo)
print(totalV)
