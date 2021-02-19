valueProduct = int(input('Informe o valor do produto: '))
desc = int(input('Porcentagem de desconto: '))
valueDesc = float(valueProduct / 100 * desc)
newValueProduct = valueProduct - valueDesc
print(f'O desconto foi de R$%.2f' % valueDesc,
      '\nPreço à pagar R$%.2f' % (newValueProduct))