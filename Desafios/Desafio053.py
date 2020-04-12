frase = str(input('Digite uma frase: ')).upper().strip().split()
junto = ''.join(frase)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print(junto, inverso)
if inverso == junto:
    print('A frase é um palindromo.')
else:
    print('A frase NÃO é um palindromo.')