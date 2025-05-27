#Calcule a média de dias entre as vendas de um mesmo produto (dica: usar defaultdict(list) para agrupar datas por produto e depois calcular diferença entre elas).

import csv
from collections import defaultdict
from datetime import datetime

# Dicionário com listas de datas por produto
vendas_por_produto = defaultdict(list)

# Lê o arquivo
with open('Vendas.csv', mode='r', encoding='utf-8', newline='') as f:
    leitor = csv.reader(f)
    next(leitor)  # pula o cabeçalho

    for linha in leitor:
        data = datetime.strptime(linha[0], "%Y-%m-%d")  # Converte a data
        produto = linha[1]
        vendas_por_produto[produto].append(data)

# Calcula a média de dias entre vendas por produto
for produto, datas in vendas_por_produto.items():
    if len(datas) < 2:
        continue  # Não dá pra calcular média com só uma data

    # Ordena as datas
    datas.sort()

    # Calcula as diferenças entre datas consecutivas
    diferencas = [
        (datas[i] - datas[i - 1]).days
        for i in range(1, len(datas))
    ]

    # Calcula a média
    media_dias = sum(diferencas) / len(diferencas)

    print(f"Produto: {produto}, Média de dias entre vendas: {media_dias:.2f}")
