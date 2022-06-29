vel = int(input('Qual a velocidade do carro? '))
if vel > 80:
    print('Você foi multado por ultrapassar o limite máximo de 80km/h')
    print('O valor da multa é de R${:.2f}'.format((vel - 80) * 7))
print('Tenha um bom dia! Dirija com segurança!')
