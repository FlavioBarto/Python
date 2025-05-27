#Filtre todas as vendas realizadas nos últimos 30 dias.

import csv
from datetime import datetime

vendas_ultimos_30_dias = []

with open('Vendas.csv', mode='r', encoding='utf-8', newline='') as f:
    leitor = csv.reader(f)
    cabecalho = next(leitor)  # Salva o cabeçalho, se quiser usar depois

    for linha in leitor:
        data_str = linha[0]
        data_venda = datetime.strptime(data_str, "%Y-%m-%d")
        data_atual = datetime.today()

        diferenca_dias = (data_atual - data_venda).days

        # Se a venda aconteceu nos últimos 30 dias
        if 0 <= diferenca_dias <= 30:
            vendas_ultimos_30_dias.append(linha)

# Exibe as vendas filtradas
for venda in vendas_ultimos_30_dias:
    print(venda)
