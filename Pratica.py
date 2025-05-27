import pandas as pd # importa a biblioteca Pandas com apelido pd


df = pd.read_csv('Pandas/vendas.csv',delimiter =',', encoding='utf-8', parse_dates=['data'])
#parse_dates é da biblioteca Pandas e altera o campo 'data' para o tipo data (para não ser reconhecido como string)
total_vendas = len(df)#conta o numero total de vendas(linhas)
print("Total de Vendas: ", total_vendas)

faturamento = df['qtd']*df['valor_unitario']
print("Faturamento: ", faturamento)