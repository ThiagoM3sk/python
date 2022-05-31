from math import radians, cos, sin, tan
ângulo = float(input('Digite o ângulo: '))
seno = sin(radians(ângulo))
print('O seno do ângulo {} é {:.2f}'.format(ângulo, seno))
cosseno = cos(radians(ângulo))
print('O cosseno do ângulo {} é {:.2f}'.format(ângulo, cosseno))
tangente = tan(radians(ângulo))
print('O tangente do ângulo {} é {:.2f}'.format(ângulo, tangente))
