valor = float(input('Digite o valor:'))
quantidade = float(input('Digite o Quantide:'))

if  quantidade < 10 :
   desconto = 0
elif quantidade < 20:
   desconto = 0.1
else:
   desconto = 0.2

vaD = quantidade * valor

vaCoD = vaD * (1 - desconto)

vf = vaD - vaCoD

vff = vaD - vf

print('valor sem desconto:',vaD)
print('valor sem desconto:',vf)
print('valor com  desconto:',vff)


