value = int(input('Informe uma nota: '))
while value < 0 or  value >  10:
  print('Informe um valor válido')
  value = int(input('Informe uma nota: '))
print(value)