#Some o total de valores da coluna preco.
import csv
soma = 0
with open('../aula/vendas_teste.csv', mode='r', encoding='utf-8',newline='') as f: #abre o arquivo csv e ve todos os dados/linhas no arquivo

    leitor = csv.reader(f, delimiter=',')
    next(leitor)

    # 4. Percorre cada linha restante do arquivo
    for linha in leitor: #o linha passa por todas as linhas no leitor
        soma += float(linha[3]) 
        print(f"{soma:.2f}")
        # print(linha[1]) #esse fica preso em uma coluna mas passa pelas linha // esse vai passar só pelos produtos

