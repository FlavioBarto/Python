#Conte quantas linhas o arquivo possui (sem contar o cabeçalho).

import csv

qtd = 0
# 1. Abre o arquivo CSV em modo de leitura
with open('aula/vendas_teste.csv', mode='r', encoding='utf-8',newline='') as f: 

    leitor = csv.reader(f, delimiter=',')

    header = next(leitor)
    print('Colunas encontradas:', header)
    # 4. Percorre cada linha restante do arquivo
    for linha in leitor:
        
        qtd = qtd + 1
        print(qtd)
