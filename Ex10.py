lado1 = int(input("Insira o primeiro lado "))
lado2 = int(input("Insira o segundo lado "))
lado3 = int(input("Insira o terceiro lado "))

if lado1 == lado2 and lado1 == lado3 :
    print("Triângulo Equilátero")
elif (lado1 == lado2 or lado2 == lado3 or lado1 == lado3) :
    print("Triângulo Isósceles")
else :
    print("Trângulo Escaleno")
