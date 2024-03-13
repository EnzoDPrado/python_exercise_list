number1 = int(input("Insira um numero "))
number2 = int(input("Insira um numero "))
number3 = int(input("Insira um numero "))
aux = 0

if number1 > number2 and number1 > number3:
    aux = number3
    number3 = number1
    number1 = aux
elif number2 > number3:
    aux = number3
    number3 = number2
    number2 = aux

print(f"Maior numero {number3}")
