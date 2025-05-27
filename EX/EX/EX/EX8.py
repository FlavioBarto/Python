#Calcule a média de preços dos produtos.

import csv
qtd = 0
preco = 0

with open('../aula/vendas_teste.csv', mode = 'r', encoding='utf-8',newline='') as f:
    leitor = csv.reader(f, delimiter=',')
    header = next(leitor)

    for linha in leitor:
        preco += float(linha[3])
        qtd = qtd + 1

    print(f"resuldado: {float((preco/qtd)):.2f}")

