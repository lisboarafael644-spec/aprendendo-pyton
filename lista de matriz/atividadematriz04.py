vendas = [
    [1200, 850, 900, 1500],
    [900, 1100, 1000, 1300],
    [1500, 1600, 1400, 1800],
    [700, 600, 800, 900]
]
vendas_vendedores = []
for vendor in vendas:
    total_vendas = 0
    for dias in vendor:
        total_vendas += dias
    vendas_vendedores.append(total_vendas)
print(f"Total de vendas: {vendas_vendedores}")