#Crie uma nova lista com apenas as vendas feitas no mês de maio.

import csv
from datetime import datetime

vendas_maio = []

with open('Vendas.csv', mode='r', encoding='utf-8', newline='') as f:
    leitor = csv.reader(f)
    cabecalho = next(leitor)  # Se quiser salvar também

    for linha in leitor:
        data_str = linha[0]
        data_obj = datetime.strptime(data_str, "%Y-%m-%d")
        
        if data_obj.month == 5:
            vendas_maio.append(linha)

# Exibe as vendas de maio
for venda in vendas_maio:
    print(venda)
