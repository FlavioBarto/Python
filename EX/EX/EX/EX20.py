#Calcule a diferença em dias entre cada data e a data atual.

import csv
from datetime import datetime

with open('Vendas.csv', mode='r', encoding='utf-8', newline='') as f:
    leitor = csv.reader(f)
    next(leitor)  # Pula o cabeçalho

    for linha in leitor:
        data_str = linha[0]
        data_venda = datetime.strptime(data_str, "%Y-%m-%d")  # Converte string em datetime
        data_atual = datetime.today()  # Data atual do sistema
        diferenca = (data_atual - data_venda).days  # Diferença em dias

        print(f'Data da venda: {data_str}, Dias desde a venda: {diferenca}')