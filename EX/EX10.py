#Crie uma lista de dicionários (um por linha) a partir do CSV lido manualmente.

import csv
dados = []

with open('../aula/vendas_teste.csv', mode = 'r', encoding='utf-8',newline='') as f:
    leitor = csv.reader(f)
    header = next(leitor)

    for linha in leitor:
        lista = {}
        for i in range(len(header)):
            lista[header[i]] = linha[i].strip()
        dados.append(lista)

for item in dados[:5]: #tem esse dois pontos para indicar que vai até a posição 5 na lista
    print(item)
