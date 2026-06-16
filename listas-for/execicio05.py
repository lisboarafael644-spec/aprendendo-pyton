peso = float(input("seu peso:"))
altura = float(input("sua altura:"))

imc = peso / (altura * altura)

if imc < 18.5:
    print("Abaixo")
elif imc < 25:
    print("normal")
elif imc < 30:
    print("sobrepeso")
else:
    print("obeso")