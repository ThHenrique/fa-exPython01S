value1 = int(input('Informe um valor: '))
value2 = int(input('Informe um valor: '))

while value1 % value2 != 0:
  value1, value2 = value2, value1%value2
print(value2)