#Use Counter para encontrar o produto mais vendido.

import csv
from collections import Counter

contador_produtos = Counter()

with open('../aula/vendas_teste.csv', mode='r', encoding='utf-8', newline='') as f:
    leitor = csv.reader(f, delimiter=',')
    next(leitor)  # Pula o cabeçalho

    for linha in leitor:
        quantd = linha[1]
        contador_produtos[quantd] += 1

mais_vendido = contador_produtos.most_common(1)[0]
print(f'Produto mais vendido: {mais_vendido[0]} (vendido {mais_vendido[1]} vezes)')


