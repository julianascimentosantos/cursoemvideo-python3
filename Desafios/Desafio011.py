b = float(input('Largura da parede: '))
h = float(input('Altura da parede: '))
a = b*h
t = a*0.5
print('Sua parede tem a dimensão de {}x{} e sua área é de {}.'.format(b, h, a))
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(t))