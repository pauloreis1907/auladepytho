def adicao(a,b):
 return a+b
def subritacao(a,b):
 return a-b
def nultiplicacao(a,b):
 return a*b
def divisao(a,b):
 return a*b
 if b ==0:
   return " erro Divisão por zero"
 return a/b
def calculadora():
    print('escolha a operaçao')
    print('1 adiçao')
    print('2 subtração')
    print('3 multiplicação')
    print('4 divisÃO')
    esc = int(input('Digite o numero da operaçao'))
    num1 = float (input("Digite o primeiro numero:"))
    num2 = float (input("Digite o primeiro segunto:"))

    if esc == 1:
        resul = num1 + num2
        print(f'resultado:',resul)
    elif esc == 2:
        resul = num1 - num2
        print(f'resultado?',resul)
    elif esc == 3:
        resul = num1 * num2
        print(f'resultado:',resul)
    elif esc == 4:
        resul = num1 / num2
        print(f'resultado:',resul)
    else:
        print('operação invalidade')

calculadora()
