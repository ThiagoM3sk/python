salario = float(input('Digite seu salário atual: R$'))
aumento = salario + (salario*15/100)
print('Seu salário era R${:.2f}, agora com um aumento de 15% está R${:.2f}'.format(salario, aumento))
