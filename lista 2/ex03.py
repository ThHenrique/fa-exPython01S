kg= float(input("Digite o peso total dos peixes em kg: "))

if kg > 50:
  punicao = (kg - 50) * 4
  excesso = kg - 50
  print(f'A quantidade de peixe que você possui ultrapassou {excesso:.2f} kg. você será multado em {punicao:.2f} reais')

else :
  print ("Você está dentro dos limites de quantidade de peixes, você está liberado, tenha um bom dia!")