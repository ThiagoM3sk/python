salario = float(input('Qual seu salário atualmente? '))
if salario <= 1250:
    newSalario = salario + (salario * 15 / 100)
    print('Seu salário vai receber um aumento de 15% e agora você irá receber R$ {:.2f}'.format(newSalario))
else:
    newSalario = salario + (salario * 10 / 100)
    print('Seu salário recebeu um aumento de 10% e agora você irá receber R$ {:.2f}'.format(newSalario))
print('Aproveite seu novo salário!')
