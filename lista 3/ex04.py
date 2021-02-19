print('*='*15)
print('Sequencia de Fibonacci')
print('*='*15)
x = int(input('informe um número inteiro: '))
t1 = 0
t2 = 1
print('=='*30)
print(f'{t1} -> {t2} -> ', end="")
count = 3
while count <= x:
  t3 = t1 + t2
  print(f'{t3} -> ', end="")
  t1, t2 = t2, t3
  count += 1
print(f'Número de Fibonacci = {t3}')


