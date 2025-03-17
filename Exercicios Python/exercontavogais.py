def contavagais(palavra):
    vogais = 'aeiouAEIOU'
    contagem =  0
    for vogal in palavra:
        if vogal in vogais:
            contagem+=1
    return contagem
palavra = str(input('digite a palavra:'))
print(contavagais(palavra))


