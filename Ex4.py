appleValue = 0
appleQuantity = int(input("Insira a quantidade de maçãs que deseja comprar! "))

if appleQuantity < 12:
    appleValue = 0.30
else:
    appleValue = 0.25

print(f"Valor total da compra: {appleValue}")
