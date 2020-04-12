import math
grau = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(grau))
print('O ângulo de {} tem o SENO de {:.2f}'.format(grau, seno))
print('O ângulo de {} tem o COSENO de {:.2f}'.format(grau, math.cos(math.radians(grau))))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(grau,math.tan(math.radians(grau))))