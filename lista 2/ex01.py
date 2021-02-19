r1 = float(input("Primeiro seguimento :"))
r2 = float (input("Segundo seguimento :"))
r3 = float (input ("terceiro seguimento :"))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print ("Os seguimentos acima podem formar um triângulo!", end = " ")

    if r1 == r2 == r3:
        print ("E ele um triângulo equilátero")

    elif r1 != r2 != r3 != r1 :
        print ("E ele um triângulo escaleno")

    else:
        print ("E ele um triângulo isoceles") 
else: 
  print('Não é triângulo')
