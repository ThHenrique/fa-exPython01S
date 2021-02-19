cDia = int(input('Cigarros fumados por dia: '))
cAnos = int(input('Há quantos anos você fuma? '))
total = cDia * 365 * cAnos // 144
print(f'Vocês perdeu {total} dias de vida')