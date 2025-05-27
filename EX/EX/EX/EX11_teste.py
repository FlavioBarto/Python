#Use Counter para contar a frequência de produtos vendidos no arquivo vendas.csv.
import csv
from collections import Counter

# Cria um contador para armazenar a soma das quantidades por produto
contador_produtos = Counter()

with open('../aula/vendas_teste.csv', mode='r', encoding='utf-8') as f:
    leitor = csv.reader(f)
    next(leitor)  # pula o cabeçalho

    for linha in leitor:
        produto = linha[1].strip().lower()
        quantidade = int(linha[2])
        contador_produtos[produto] += quantidade

# Exibe os resultados
for produto, total in contador_produtos.items():
    print(f'Produto: {produto}, Quantidade total vendida: {total}')