#Ordene os produtos por quantidade total vendida (do maior para o menor).

import csv
from collections import defaultdict
qtd = defaultdict(int)

with open('Vendas.csv', mode='r', encoding='utf-8', newline='') as f:
    leitor = csv.reader(f, delimiter=',')
    next(leitor)  
    for linha in leitor:
        nome_produto = linha[1]
        qtd[nome_produto] += int(linha[2])

ordenado = sorted(qtd.items(), key=lambda item: item[1], reverse=True) 


for produto, total_qtd in ordenado:
 print(f'Produto: {produto}, Quantidade total vendida: {total_qtd}')

#for linha in leitor:
   