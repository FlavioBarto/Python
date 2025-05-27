#Leia a lista de vendas (produto, quantidade) e use defaultdict(int) para somar o total de unidades vendidas por produto.
import csv
from collections import defaultdict
produto = {}
quantidade = {}
soma = defaultdict(int)

with open('../aula/vendas_teste.csv', mode='r', encoding='utf-8', newline='') as f:
    leitor = csv.reader(f, delimiter=',')
    next(leitor)  # Pula o cabeçalho

    for linha in leitor:
        produto = linha[1]
        quantidade = int(linha[2])

        soma[produto] += quantidade

for produto, total in soma.items():
    print(f'Produto: {produto}, Total vendido: {total}')
