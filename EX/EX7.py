#Grave todas as linhas cujo preço seja maior que 100 em um novo arquivo alto_valor.csv.

import csv
nome_arquivo = "alto_valor.csv"

with open('../aula/vendas_teste.csv', mode = 'r', encoding='utf-8',newline='') as f:
    leitor = csv.reader(f, delimiter=',')
    header = next(leitor)

    with open('alto_valor.csv', mode='w', encoding='utf-8',newline='') as arquivo:
        escritor = csv.writer(arquivo)

        escritor.writerow(header)
        for linha in leitor:
                if float(linha[3]) > 100.00:
                    escritor.writerow(linha)  # Grava a linha no novo arquivo






