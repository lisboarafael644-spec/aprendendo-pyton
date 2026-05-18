salario = float(input("digite seu salario:"))
parcelas = float(input("digite sua parcelas:"))

limite = salario * 0.3

if parcelas <= limite:
    print("credito aprovado")
else:
    print("credito recusado")