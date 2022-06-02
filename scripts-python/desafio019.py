from random import choice
primeiro = input('Nome do primeiro aluno: ')
segundo = input('Nome do segundo aluno: ')
terceiro = input('Nome do terceiro aluno: ')
quarto = input('Nome do quarto aluno: ')
lista = [primeiro, segundo, terceiro, quarto]
escolhido = choice(lista)
print('O sorteado foi {}'.format(escolhido))
