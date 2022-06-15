#minha resolução
#city = str(input('Digite o nome da sua cidade: ')).strip().capitalize()
#santo = city.split()
#print('Sua cidade começa com a palavra Santo? {}'.format('Santo' in santo[0]))

#resolução do professor
cid = str(input('Digite o nome da sua cidade: ')).strip()
print(cid[:5].upper() == 'SANTO')