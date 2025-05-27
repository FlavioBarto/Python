#Use Counter para contar a frequência de produtos vendidos no arquivo vendas.csv.

import csv
from collections import Counter
qtd_itens_vend = Counter()
produto = []
quantidade = 0
with open('../aula/vendas_teste.csv', mode='r', encoding='utf-8', newline='') as f:
    leitor = csv.reader(f, delimiter=',')
    next(leitor)
    for linha in leitor:
        produto = linha[1]
        quantidade = int(linha[2])
        qtd_itens_vend[produto] += quantidade

for produto, quantidade in qtd_itens_vend.items():
    print(f'Produto: {produto}, Quantidade: {quantidade}')
