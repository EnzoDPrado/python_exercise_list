numeroLados = int(input("Insira a quantidade de lados do seu polígno"))
medidaLado = float(input("Insira a medida do lado"))

if numeroLados == 3 :
    print(f"TRIÂNGULO / PERIMETRO: {medidaLado * 3}")
elif numeroLados == 4 :
    print(f"QUADRADO / PERIMETRO :{medidaLado * 4}")
elif numeroLados == 5 :
    print(f"PENTÁGONO / PERIMETRO :{medidaLado * 5}")
