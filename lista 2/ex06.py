hr_tb = float(input("Horas trabalhadas por mês: "))
v_hr = float(input("Valor recebido por hora:  "))

sb = hr_tb * v_hr
inss = ((sb / 100) * 8)
ir = ((sb / 100) * 11)
sind = ((sb / 100 ) * 5)
desc = inss + ir + sind
sl = (sb - desc)
print (f'+ Salário Bruto: R${sb:.2f}')
print (f'- IR: R${ir:.2f}')
print (f'- INSS : R${inss:.2f}')
print (f'- Sindicato R${sind:.2f}')
print (f'DESCONTO TOTAL: R${desc:.2f}')
print (f'Salário Liquido R${sl:.2f}')