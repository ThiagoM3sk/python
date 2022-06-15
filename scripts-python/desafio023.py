# mina resolução
#n1 = input('Insira um valor de 0 a 9999: ')
#print('Seu número tem {} unidade(s)'.format(n1[3]))
#print('Seu número tem {} dezena(s)'.format(n1[2]))
#print('Seu número tem {} centena(s)'.format(n1[1]))
#print('Seu número tem {} milhar'.format(n1[0]))

# funcionou em partes

#resolução do professor

num = int(input('Digite um valor de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
