valor = float(input("digite o valor da compra: R$"))
if valor <= 100:
    desconto = 0
elif valor > 100 and valor <=300:
    desconto = 0.5
elif valor > 300 and valor <= 500:
    desconto = 0.5

elif not (valor <= 500):
    desconto = 0.15

ValorFinal = valor - (valor * desconto)

print(f"desconto aplicado: {desconto * 100}$")
print(f"valor final: R$ {ValorFinal:.2f}")