# minha resolução
"""salario = float(input('Qual seu salário atualmente? '))
if salario <= 1250:
    newSalario = salario + (salario * 15 / 100)
    print('Seu salário vai receber um aumento de 15% e agora você irá receber R$ {:.2f}'.format(newSalario))
else:
    newSalario = salario + (salario * 10 / 100)
    print('Seu salário recebeu um aumento de 10% e agora você irá receber R$ {:.2f}'.format(newSalario))
print('Aproveite seu novo salário!')"""
# resolução do professor
salário = float(input('Qual o salário do funcionário? R$'))
if salário <= 1250:
    novo = salário + (salário * 15 / 100)
else:
    novo = salário + (salário * 10 / 100)
print('Quem recebia R${:.2f} passa agora a receber R${:.2f}'.format(salário, novo))
