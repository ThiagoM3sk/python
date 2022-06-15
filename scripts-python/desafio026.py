frase = str(input('Digite uma frase: ')).upper().strip()
print('a letra A aparece {} vez(es)'.format(frase.count('A')))
print('a primeira vez que aparece a letra A é na posição {}'.format(frase.find('A')+1))
print('a última vez que a letra A aparece é no índice {}'.format(frase.rfind('A')+1))
