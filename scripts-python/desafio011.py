larg = float(input('Qual a largura da parede? '))
alt = float(input('Qual a altura da parede? '))
área = larg * alt
print('Sua parede tem a dimensão de {}x{} e a área é de {}m²'.format(larg, alt, área))
tinta = área / 2
print('Para pintar essa parede, você precisará de {}L de tinta'.format(tinta))
