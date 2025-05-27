import pandas as pd


produto = []
precos = pd.Series( #cria só colunas respectivas as informações fornecidas alinha data e index
    data=[59.90, 89.50, 29.00],        # valores
    index=['camisa','calça','boné']    # rótulos de linha
)
print(precos)
#-------------------------------------------------------------------------------------------------
precos = pd.Series(
    data=[59.90, 89.50, 29.00],        # valores
    index=['camisa','calça','boné']    # rótulos de linha
)
print(precos)
print('-------------------------------')
print(precos['camisa'])
print('-------------------------------')
print(precos + 10)
print('-------------------------------')
print(precos['camisa'] + 10)
#--------------------------------------------------------------------------------------------------
df = pd.DataFrame({ #crio uma planilha
    'data':       ['2025-05-18','2025-05-19','2025-05-20'],
    'produto':    ['camisa','calça','boné'],
    'quantidade': [3,2,5],
    'preco':      [59.90,89.50,29.00]
})
print(df)
#--------------------------------------------------------------------------------------------------
df = pd.read_csv('Pandas/vendas.csv',   # caminho do arquivo
                 sep=',',        # separador
                 encoding='utf-8')# leitura de arquivo e ja passa por todo arquivo que antes precisavamos de um for
#--------------------------------------------------------------------------------------------------
#esses comandos le as primeira e ultimas linhas do dataFrame ou arquivo.csv
print(df.head(10))   # primeiras 10 linhas
print('-----------------------------------------------------------')
print(df.tail(10))   # últimas 10 linhas
#--------------------------------------------------------------------------------------------------
#Informações gerais: esse comando me passa as informações de cada linha no arquivo ou dataFrame como no exemplo:

df.info()

#Exemplo:
#<class 'pandas.core.frame.DataFrame'>
#RangeIndex: 100 entries, 0 to 99
#Data columns (total 4 columns):
  #   Column      Non-Null Count  Dtype  
#---  ------      --------------  -----  
# 0   data        100 non-null    object 
# 1   produto     99 non-null     object 
# 2   quantidade  99 non-null     float64
# 3   preco       100 non-null    float64
#dtypes: float64(2), object(2)
#memory usage: 3.3+ KB
#--------------------------------------------------------------------------------------------------
#Estatísticas descritivas: Para colunas numéricas, mostra média, desvio padrão, mínimo, máximo e quartis.
print(df.describe())
df.describe()

#Exemplo:
#       quantidade       preco
#count   99.000000  100.000000
#mean     5.262626  120.074100
#std      2.768577   55.545503
#min      1.000000   15.890000
#25%      3.000000   68.625000
#50%      6.000000  126.985000
#75%      7.500000  165.955000
#max     10.000000  198.740000
#--------------------------------------------------------------------------------------------------
#Tipos de colunas: Exibe o tipo (int64, float64, object = texto, etc.).

df.dtypes
#--------------------------------------------------------------------------------------------------
#Exibe o número de linhas e colunas:
df.shape
#Exemplo:
#(100, 4)
#--------------------------------------------------------------------------------------------------
#lista de nomes de colunas: 
df.columns
#Exemplo:
#Index(['data', 'produto', 'quantidade', 'preco'], dtype='object')
#--------------------------------------------------------------------------------------------------
#.loc (por rótulo)
#Linha e coluna específicas:
print(df.loc[0, 'produto'])
print(df.loc[72, 'produto'])

#Todas as linhas, só algumas colunas:

df.loc[:, ['produto','preco']]

#Linhas que atendem condição:

df.loc[df.preco > 50]
#--------------------------------------------------------------------------------------------------
#.iloc (por posição inteira)
#Primeira linha, segunda coluna:
print(df.iloc[0, 1])
print(df.iloc[77, 1])

#Linhas 0 a 2, colunas 0 a 2:
df.iloc[0:3, 0:3]
#-------------------------------------------------------------------------------------------------
#Transformações básicas: Criar colunas novas
df['total'] = df['quantidade'] * df['preco']
print(df)

#exemplo:
#          data  produto  quantidade   preco    total
#0   2025-05-10     saia         2.0  156.82   313.64
#1   2025-04-21   camisa         NaN   76.76      NaN
#2   2025-06-19      NaN         9.0  163.29  1469.61
#3   2025-05-18   sapato         8.0   15.89   127.12
#4   2025-05-11     meia         1.0  177.48   177.48
#..         ...      ...         ...     ...      ...
#95  2025-05-31   sapato        10.0  198.46  1984.60
#96  2025-06-22  bermuda         6.0  184.96  1109.76
#97  2025-01-20   camisa         6.0   34.75   208.50
#98  2025-06-07    blusa         8.0   81.44   651.52
#99  2025-04-18   camisa        10.0  157.86  1578.60
#------------------------------------------------------------------------------------------------
#Renomear colunas:
df = df.rename(columns={'quantidade': 'qtd', 'preco': 'valor_unitario'})
print(df)
#Exemplo:
#          data  produto   qtd  valor_unitario    total
#0   2025-05-10     saia   2.0          156.82   313.64
#1   2025-04-21   camisa   NaN           76.76      NaN
#2   2025-06-19      NaN   9.0          163.29  1469.61
#3   2025-05-18   sapato   8.0           15.89   127.12
#4   2025-05-11     meia   1.0          177.48   177.48
#..         ...      ...   ...             ...      ...
#95  2025-05-31   sapato  10.0          198.46  1984.60
#96  2025-06-22  bermuda   6.0          184.96  1109.76
#97  2025-01-20   camisa   6.0           34.75   208.50
#98  2025-06-07    blusa   8.0           81.44   651.52
#99  2025-04-18   camisa  10.0          157.86  1578.60
#------------------------------------------------------------------------------------------------
#Remover colunas:
df = df.drop(columns=['total'])
print(df)

#exemplo:
#          data  produto   qtd  valor_unitario
#0   2025-05-10     saia   2.0          156.82
#1   2025-04-21   camisa   NaN           76.76
#2   2025-06-19      NaN   9.0          163.29
#3   2025-05-18   sapato   8.0           15.89
#4   2025-05-11     meia   1.0          177.48
#..         ...      ...   ...             ...
#95  2025-05-31   sapato  10.0          198.46
#96  2025-06-22  bermuda   6.0          184.96
#97  2025-01-20   camisa   6.0           34.75
#98  2025-06-07    blusa   8.0           81.44
#99  2025-04-18   camisa  10.0          157.86
#-----------------------------------------------------------------------------------------------
#Lidar com dados faltantes:

print(df.isnull().sum())          # conta valores nulos por coluna
print('-------------------------------------------------------')
df = df.fillna(0)         # preenche nulos com zero
df = df.dropna()          # remove linhas com qualquer valor nulo
print(df)
print('-------------------------------------------------------')
print(df.isnull().sum())


import pandas as pd # importa a biblioteca Pandas com apelido pd


df = pd.read_csv('Pandas/vendas.csv',delimiter =',', encoding='utf-8', parse_dates=['data'])
#parse_dates é da biblioteca Pandas e altera o campo 'data' para o tipo data (para não ser reconhecido como string)
total_vendas = len(df)#conta o numero total de vendas(linhas)
print("Total de Vendas: ", total_vendas)
#----------------------------------------------------------------------
faturamento = (df['quantidade']*df['preco']).sum()
print("Faturamento: ", faturamento)
#----------------------------------------------------------------------
valor_Medio = faturamento / total_vendas
print("valor medio de ganho: ", valor_Medio)
#----------------------------------------------------------------------
top3 =df['produto'].value_counts().head(3)
print(top3)
#----------------------------------------------------------------------
top5 = df.nlargest(5, 'valor_total')
print("Top5: ", top5)
#----------------------------------------------------------------------
abril = df.loc[df['data'].dt.month == 4]
relatorio_abril = abril.copy()

relatorio_abril.to_csv('relatiorio_abril.csv')





