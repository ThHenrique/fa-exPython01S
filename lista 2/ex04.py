print('**'*20)
num1 = int(input('Digite um número: '))
num2 = int(input('Digite um número: '))
num3 = int(input('Digite um número: '))
print('**'*20)

if num1 > num2 and num1 > num3:
  print(f'{num1} é o maior')
if num2 > num1 and num2 > num3:
  print(f'{num2} é o maior')
if num3 > num1 and num3 > num2:
  print(f'{num3} é o maior')