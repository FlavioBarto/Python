#Use Counter para contar quantas vezes cada data aparece no arquivo.

import csv
from collections import Counter

datas = []

with open('Vendas.csv', mode='r', encoding='utf-8', newline='') as f:
    leitor = csv.reader(f)
    next(leitor)  # Pula o cabeçalho

    for linha in leitor:
        data = linha[0]
        datas.append(data)

# Conta quantas vezes cada data aparece
contagem_datas = Counter(datas)

# Exibe o resultado
for data, ocorrencias in contagem_datas.items():
    print(f'{data}: {ocorrencias} ocorrência(s)')