num1 = int(input('digite o numero:'))
num2 = int(input('digte o numero:'))

soma = num1+num2

if soma > 20:
    print('a soma é maior:', soma)
    soma = soma + 8
    print(' a nova soma:', soma)
else:
    print(' a soma é menor', soma)
    soma = soma - 5
    print(' o nova soma', soma)