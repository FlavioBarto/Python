#Use defaultdict(list) para agrupar os preços praticados por produto.
import csv
from collections import defaultdict
precos = defaultdict(float)

total = 0

with open('../Vendas.csv', mode='r', encoding='utf-8', newline='') as f:
    leitor = csv.reader(f, delimiter=',')
    next(leitor)  
    for linha in leitor:
        nome_produto = linha[1]
        precos[nome_produto] += float(linha[3])

        
for produto, total in precos.items():
    print(f'Produto: {produto}, Total vendido: {total}')
