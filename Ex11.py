lado1 = int(input("Insira o primeiro angulo "))
lado2 = int(input("Insira o segundo angulo "))
lado3 = int(input("Insira o terceiro angulo "))

if lado1 == 90 or lado2 == 90 or lado3 == 90 :
    print("Triangulo Retangulo")
elif lado1 > 90 or lado2 > 90 or lado3 > 90 :
    print("Triangulo Obtusangulo")
else :
    print("Trinângulo Acutângulo")
