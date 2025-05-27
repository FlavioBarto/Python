import csv


# 1. Abre o arquivo CSV em modo de leitura
with open('../aula/vendas_teste.csv', mode='r', encoding='utf-8',newline='') as f: #abre o arquivo csv e ve todos os dados/linhas no arquivo
    # 2. Crie um leitor CSV que separa campos por vírgula
    leitor = csv.reader(f, delimiter=',') # lê e separa pelo dilimiter ','
    # 3. Le a primeira linha (cabeçalho) para obter os nomes das colunas
    header = next(leitor)
    print('Colunas encontradas:', header)
    # 4. Percorre cada linha restante do arquivo
    for linha in leitor:
        # 5. Emparelha nomes de colunas e valores em um dicionário
        ordem = dict(zip(header, linha))
        # 6. Acessa valores pelas chaves e exiba-os
        print(f"Data: {ordem['Data']} |Produto: {ordem['produto']} | Quantidade: {ordem['quantidade']} | Preço: {ordem['preco']}")






