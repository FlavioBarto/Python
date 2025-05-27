#Conte quantas vezes cada produto aparece no arquivo usando dicionário comum.
import csv

# Dicionário para contar quantas vezes cada produto aparece
contagem = {}

# Abre o arquivo CSV
with open('../aula/vendas_teste.csv', mode='r', encoding='utf-8', newline='') as f:
    leitor = csv.reader(f, delimiter=',')

    # Lê o cabeçalho e padroniza os nomes das colunas (remove espaços e coloca em minúsculo)
    header = [col.strip().lower() for col in next(leitor)]

    # Para cada linha, cria um dicionário com os dados
    for linha in leitor:
        produto = linha[1].strip()  # usa .get() para evitar erro se não existir a chave
        if produto:
            if produto in contagem:
                contagem[produto] += 1
            else:
                contagem[produto] = 1

# Mostra o resultado
for produto, quantidade in contagem.items():
    print(f"Produto: {produto}, Quantidade: {quantidade}")


