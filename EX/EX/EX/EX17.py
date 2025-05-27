#Com base nas vendas, crie um dicionário que mapeia o produto para o número de vendas distintas.

import csv
from collections import defaultdict

# Dicionário para contar o número de vendas distintas por produto
vendas_distintas = defaultdict(int)

with open('Vendas.csv', mode='r', encoding='utf-8', newline='') as f:
    leitor = csv.reader(f)
    next(leitor)  # Pula o cabeçalho

    for linha in leitor:
        nome_produto = linha[1]
        vendas_distintas[nome_produto] += 1  # Cada linha representa uma venda

# Exibe o resultado
for produto, num_vendas in vendas_distintas.items():
    print(f'{produto}: {num_vendas} vendas distintas')
