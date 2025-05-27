#Agrupe as vendas por mês (sem Pandas) e conte quantas vendas ocorreram em cada mês.

import csv
from datetime import datetime
from collections import Counter

vendas_por_mes = Counter()

with open('Vendas.csv', mode='r', encoding='utf-8', newline='') as f:
    leitor = csv.reader(f)
    next(leitor)  # Pula o cabeçalho

    for linha in leitor:
        data_str = linha[0]  # Ex: '2025-05-10'
        data_obj = datetime.strptime(data_str, "%Y-%m-%d")
        mes = data_obj.strftime("%Y-%m")  # Ex: '2025-05'

        vendas_por_mes[mes] += 1

# Exibe o resultado
for mes, total in sorted(vendas_por_mes.items()):
    print(f'{mes}: {total} venda(s)')