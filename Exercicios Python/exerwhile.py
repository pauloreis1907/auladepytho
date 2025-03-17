
quantidadeImpares = 0
quantidadePares = 0

for i in range(5):

    num= int(input('Digite o numero:'))

    if num % 2 == 0 :
        quantidadePares  += 1

    else:
        quantidadeImpares  += 1

print('numero pares', quantidadePares)
print(f'numeros impares {quantidadeImpares}')

#Paulo victor dos reis