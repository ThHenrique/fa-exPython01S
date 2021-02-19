import random
lista1 = random.sample(range(100), 10)
lista2 = random.sample(range(100), 10)
lista = []

print(lista1)
print(lista2)

for x in range(10):
  lista.append(lista1[x])
  lista.append(lista2[x])

print(lista)