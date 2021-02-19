print('**'*18)
print('Ano bissexto: ')

ano = int(input('Informe o ano para ser analisado: '))

if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):  
  print("Bissexto")
else: print('Não bissexto')
  