# Converta a string da coluna data (formato YYYY-MM-DD) em objetos datetime.

import csv
from datetime import datetime

datas_convertidas = []

with open('Vendas.csv', mode='r', encoding='utf-8', newline='') as f:
    leitor = csv.reader(f)
    next(leitor)  # Pula o cabeçalho

    for linha in leitor:
        data_str = linha[0]
        data_obj = datetime.strptime(data_str, "%Y-%m-%d")  # Converte para datetime
        datas_convertidas.append(data_obj)

# Exibe algumas datas convertidas
for data in datas_convertidas[:5]:
    print(data)