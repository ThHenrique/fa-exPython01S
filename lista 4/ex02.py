import random
lista = random.sample(range(100), 20)
pares = []
impares = []

for x in lista:
  if x % 2 == 0:
    pares.append(x)
  else :
    impares.append(x)

print(f'{lista} - Números Sorteados ')
print(f'{pares} - Número Pares')
print(f'{impares} - Números Impares')
