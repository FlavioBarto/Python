# Crie uma nova lista contendo somente as vendas em que a quantidade foi maior que 5.

import csv
from collections import defaultdict

maior5 = []

with open('Vendas.csv', mode='r', encoding='utf-8', newline='') as f:
    leitor = csv.reader(f, delimiter=',')
    next(leitor)  

    for linha in leitor:
        qtd = int(linha[2])
        if qtd > 5:
            maior5.append(linha)

for venda in maior5:
    print(venda)