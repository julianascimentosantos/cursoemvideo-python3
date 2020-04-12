'''co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjavente: '))
print('A hipotenusa vai medir {:.2f}'.format(((co**2)+(ca**2))**(1/2)))'''

import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjavente: '))
print('A hipotenusa vai medir {:.2f}'.format(math.hypot(co, ca)))