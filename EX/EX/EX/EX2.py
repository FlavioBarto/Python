#Exiba apenas o nome do produto e o preço de cada linha.
import csv

with open('aula/vendas_teste.csv', mode='r', encoding='utf-8',newline='') as f:
    leitor = csv.reader(f, delimiter=',')
    header = next(leitor)
    print('Colunas encontradas:', header)
    for linha in leitor:
        ordem = dict(zip(header, linha))
        print(f"Produto: {ordem['produto']} | Preço: {ordem['preco']}")