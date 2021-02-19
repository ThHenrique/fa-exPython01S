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
count = 0

def verifyWord(word):  
    for letra in word:
      if letra in 'python' and len(word) > 4:
        return True
    return False
    
for word in frase:
  if verifyWord(word):
    result.append(word)

print(len(result))

