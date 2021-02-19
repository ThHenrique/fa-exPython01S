salario = int(input('Informe seu salário: '))
aumento = int(input('Porcentagem de aumento: '))
valueSalary = float(salario / 100 * aumento)
newSalaray = salario + valueSalary
print(f'Seu aumento foi de R$%.2f' % valueSalary,
      'e\nseu novo salário é de R$%.2f' % (newSalaray))