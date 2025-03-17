with open('texto.txt','w', encoding='utf-8') as file:
    for i in range(3):
        frase = input(f'digite{i+1}ª frase:')
        file.write(frase+'\n')

print('FRASES SALVAS COM SUCESSO!')

with open('texto.txt','r', encoding='utf-8') as file:
   print(file.read())
