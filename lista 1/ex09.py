km = int(input('Kilômetros corridos com o carro: '))
dia = int(input('dias alugados: '))
total = km * 0.15 + dia * 60
print(f'Preço à pagar: R$ {total:.2f} ')