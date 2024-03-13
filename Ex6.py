sexoPessoa = int(input("Qual o seu sexo (1: F 2: M)"))
alturaPessoa = float(input("Insira a sua altura ex: 1.80"))
pesoIdeal = 0

if(sexoPessoa == 1):
    pesoIdeal = (62.1 * alturaPessoa) - 44.7
else :
    pesoIdeal = (72.7 * alturaPessoa) - 58

print(f"O seu peso ideial é: {pesoIdeal}")
