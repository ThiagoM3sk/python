n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
# verificando quem é  menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and  n3 < n2:
    menor = n3
# verificando quem é o maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O menor valor foi o {}'.format(menor))
print('O maior valor foi o {}'.format(maior))
