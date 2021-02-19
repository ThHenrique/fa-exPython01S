print('**'*20)
metros = float(input('M² a ser pintado: '))
print('=='*20)
if metros % 54 == 0:
  latas = metros / 54
  vTotal = latas * 80
  print(f'Serão utilizadas {latas:.0f} lata(s). Total R$ {vTotal:.2f}')
else:
  latas =( metros / 54) + 1
  vTotal = latas * 80
  print(f'Serão utilizadas {latas:.0f} lata(s). Total R$ {vTotal:.2f}')


