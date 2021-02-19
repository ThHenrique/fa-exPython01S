frase = '''The Python Software Foundation and the global Python
community welcome and encou
rage participation by everyone. Our community is based on
mutual respect, tolerance, and encouragement, and we are working to help each other live up
to these principles. We want our community to be more diverse: whoever you are, and
whatever your backgrou
nd, we welcome you.'''

frase = frase.lower()
frase = frase.replace(',', ' ')
frase = frase.replace('.', ' ')
frase = frase.replace(':', ' ')
frase = frase.split()

result = []
for palavra in frase:
  if palavra[0] in 'python' or palavra[-1] in 'python':
    result.append(palavra)

print(result)

