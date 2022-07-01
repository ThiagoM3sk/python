viagem = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}Km'.format(viagem))
if viagem <= 200:
    print('Sua passagem custou R${:.2f}'.format(viagem * 0.5))
else:
    print('Sua passagem custou R${:.2f}'.format(viagem * 0.45))
print('Boa viagem!')
