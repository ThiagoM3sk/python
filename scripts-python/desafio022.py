# minha resolução
#nome = input('Digite seu nome completo: ')
#print('Seu nome apenas em maiúsculas fica {}'.format(nome.upper()))
#print('Seu nome apenas em minúsculas fica {}'.format(nome.lower()))
#comp = nome.split()
#print('Seu nome completo contém {} caracteres'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome contém {} caracteres'.format(len(comp[0])))

# resolução do professor
nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas tem {}'.format(nome.upper()))
print('Seu nome em minúsculas tem {}'.format(nome.lower()))
print('Seu nome ao todo tem {} letras'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e tem {} letras'.format(separa[0], len(separa[0])))
