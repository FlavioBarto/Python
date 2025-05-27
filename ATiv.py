import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('/content/dados_estatistica_visualizacao.csv', sep=',', encoding='utf-8')

media_idade = df['idade'].mean()
media_salario = df['salario'].mean()

#Média
df['idade'].mean() #mean significa a media então apenas mostra a media somada


#mediana
df['idade'].median() #vai mostrar a mediana


#moda
df['idade'].mode() #vai mostrar a moda


#desvio padrão
df['idade'].std()


#variância
df['idade'].var()


#Amplitude (max - min)
df['idade'].max() - df['idade'].min() #o maximo de idade menos o minimo de idade


def faixa_etaria(idade):
  if idade <= 25:
    return "Jovem"
  elif idade <= 50:
    return "Adulto"
  else:
    return "Senior"

df['faixa_etaria'] = df['idade'].apply(faixa_etaria)
print(df['faixa_etaria'].value_counts())

#Gráfico de barras com a distribuição por estado.

sns.countplot(x='estado', data=df) #faz um grafico de barras com base no dataframe pego pelo pandas no arquivo pedido
plt.title("Distribuição por estado") #
plt.ylabel("Estados")
plt.show()

#Boxplot de salário por departamento.
sns.boxplot(x='departamento', y='salario', data=df)
plt.title("Distribuição por estado")
plt.ylabel("departamento")
plt.xlabel("salario")
plt.show()

#Gráfico de dispersão entre idade e salario, colorido por departamento.

sns.scatterplot(x='idade', y='salario', hue='departamento', data=df)
plt.title("Idade x Salario por deparatamentos")
plt.show