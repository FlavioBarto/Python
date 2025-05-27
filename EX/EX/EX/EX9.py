#Exiba a maior e a menor quantidade vendida no arquivo. #pesquisar como fazer mostrando o produto vendido
import csv

quantidades = []

with open('../aula/vendas_teste.csv', mode='r', encoding='utf-8', newline='') as f:
    leitor = csv.reader(f, delimiter=',')
    next(leitor)  # Pula o cabeçalho

    for linha in leitor:
        try:
            qtd = int(linha[2])  # Coluna quantidade
            quantidades.append(qtd)
        except (ValueError, IndexError):
            continue  # Ignora linhas inválidas

if quantidades:
    print(f'Maior quantidade vendida: {max(quantidades)}')
    print(f'Menor quantidade vendida: {min(quantidades)}')
else:
    print("Nenhuma quantidade válida encontrada.")


