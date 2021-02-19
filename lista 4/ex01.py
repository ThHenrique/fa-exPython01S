import random
lista = random.sample(range(100), 10)   #amostragem -- pega 10 números aleatórios de 1 a 100
menor = maior = lista[0]
print("Números sorteados ", end="")
for x in lista:
  print(f'{x} -> ', end="")
  if x < menor:
    menor = x
  if x > maior:
    maior = x
print('\n')
print(f'Maior número {maior} ', end="")
print(f'Menor Número {menor}')
