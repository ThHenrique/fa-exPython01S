dia = int(input('Informe a quantidade dias: '))
horas = int(input('Horas: '))
minutos = int(input('Minutos: '))
segundos = int(input('Segundos: '))
segundosTotal = segundos + (minutos * 60) + (horas * (60 * 60)) + dia * (24 * (60 * 60))
print(
    f'{dia} dia, {horas} horas, {minutos} minutos e {segundos}\n é equivalente à {segundosTotal} segundos'
)
