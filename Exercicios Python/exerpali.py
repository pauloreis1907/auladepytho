p = str (input('Digite uma palavra:'))

if p == p[::-1]: #verificar a palavra
    print('é:palindrom',p)
else:
    print('não é:palindromo',p)