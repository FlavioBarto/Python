import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

df = pd.read_csv('Life_Expectancy_Data.csv', sep=',', encoding='latin1')
df.columns = [col.strip().replace('�','a').replace('ã','a').replace('ç','c').replace('á','a').replace(' ', '') for col in df.columns]
paises_unicos = sorted(df['Country'].unique())
pais_selecionado = st.sidebar.selectbox("Escolha o país que deseja analisar:", paises_unicos)
df_pais = df[df['Country'] == pais_selecionado]

#-----------------------------------------------------
st.write("Os vários fatores de previsão inicialmente escolhidos realmente afetam a expectativa de vida, Quais são as variáveis de previsão que realmente afetam a expectativa de vida")
st.subheader("Quais são as variaveis que afetam a expectativa de vida", divider=True)
pais = df_pais
pais2 = pais.sort_values(by='Year', ascending=True)
st.write(pais2)

st.subheader(f"Evolução da Expectativa de Vida em {pais_selecionado}", divider=True)

fig, ax = plt.subplots(figsize=(20, 10))
sns.lineplot(data=df_pais, x='Year', y='Lifeexpectancy', marker='o', ax=ax)
ax.set_ylabel("Expectativa de Vida")
ax.set_xlabel("Ano")
ax.set_title(f"Expectativa de Vida em {pais_selecionado} ao longo do tempo")
st.pyplot(fig)

df_pais = df[df['Country'] == pais_selecionado].sort_values('Year')

# Gráfico de linha: Gasto com saúde ao longo do tempo
st.subheader(f"Evolução do Gasto com Saúde em {pais_selecionado}", divider=True)

fig, ax = plt.subplots(figsize=(20, 10))
sns.lineplot(data=df_pais, x='Year', y='Totalexpenditure', marker='o', ax=ax)
ax.set_ylabel("Gasto Total com Saúde (% do PIB)")
ax.set_xlabel("Ano")
ax.set_title(f"Gasto com Saúde ao longo dos anos em {pais_selecionado}")
st.pyplot(fig)


st.subheader(f"Expectativa de Vida e Escolaridade ao longo dos anos em {pais_selecionado}", divider=True)

fig, ax1 = plt.subplots(figsize=(20, 10))

# Linha 1: Expectativa de Vida
sns.lineplot(data=df_pais, x='Year', y='Lifeexpectancy', ax=ax1, label='Expectativa de Vida', color='blue')
ax1.set_ylabel('Expectativa de Vida', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

# Eixo Y secundário para Escolaridade
ax2 = ax1.twinx()
sns.lineplot(data=df_pais, x='Year', y='Schooling', ax=ax2, label='Escolaridade', color='orange')
ax2.set_ylabel('Escolaridade (anos)', color='orange')
ax2.tick_params(axis='y', labelcolor='orange')

ax1.set_title(f"Evolução da Expectativa de Vida e Escolaridade em {pais_selecionado}")
st.pyplot(fig)

st.write("as variaveis que realmente mudariam a expectativa de vida são os gastos com saude, educação, IMC populacional")
#-----------------------------------------------------
#Um país com menor expectativa de vida (<65) deve aumentar seus gastos com saúde para melhorar sua expectativa de vida média?
# Filtrar apenas o ano de 2015
#fazer uma tabela que vê o gasto em saude de paises com mais de 65 de espectativa de vida e oa com menos
# Filtrar os países com expectativa >= 65 e < 65
dfPaismais65 = df[df['Lifeexpectancy'] >= 65]
dfPaismenos65 = df[df['Lifeexpectancy'] < 65]

fig, ax = plt.subplots(figsize=(20, 5))
sns.histplot(dfPaismais65['percentageexpenditure'], kde=True, color='blue', label='>= 65')
sns.histplot(dfPaismenos65['percentageexpenditure'], kde=True, color='red', label='< 65')
ax.set_title('Distribuição dos Gastos em Saúde')
ax.set_xlabel('Gasto em Saúde (% do PIB)')
ax.set_xlim(0, 500)  # Limita a visualização até 500 (ajuste conforme os dados reais)
ax.legend()
st.pyplot(fig)

#----------------------------------------------------
#Como as taxas de mortalidade infantil e adulta afetam a expectativa de vida?

# Gráfico 1: Mortalidade Infantil vs Expectativa de Vida
fig1, ax1 = plt.subplots()
sns.regplot(data=df, x='infantdeaths', y='Lifeexpectancy', ax=ax1, scatter_kws={'alpha': 0.5})
ax1.set_title('Impacto da Mortalidade Infantil na Expectativa de Vida')
ax1.set_xlabel('Mortalidade Infantil')
ax1.set_ylabel('Expectativa de Vida')
st.pyplot(fig1)

fig2, ax2 = plt.subplots()
sns.regplot(data=df, x='AdultMortality', y='Lifeexpectancy', ax=ax2, scatter_kws={'alpha': 0.5})
ax2.set_title('Impacto da Mortalidade Adulta na Expectativa de Vida')
ax2.set_xlabel('Mortalidade Adulta')
ax2.set_ylabel('Expectativa de Vida')
st.pyplot(fig2)
#----------------------------------------------------
#A expectativa de vida tem correlação positiva ou negativa com hábitos alimentares, estilo de vida, exercícios, fumo, consumo de álcool etc.

# Gráfico: Correlação com expectativa de vida
st.subheader("Correlação entre Estilo de Vida e Expectativa de Vida", divider=True)
fig, axs = plt.subplots(2, 2, figsize=(16, 12))
# 1. Consumo de álcool
sns.regplot(data=df, x='Alcohol', y='Lifeexpectancy', ax=axs[0, 0], scatter_kws={'alpha': 0.5}, line_kws={'color': 'red'})
axs[0, 0].set_title('Álcool vs Expectativa de Vida')
# 2. IMC (alimentação)
sns.regplot(data=df, x='BMI', y='Lifeexpectancy', ax=axs[0, 1], scatter_kws={'alpha': 0.5}, line_kws={'color': 'green'})
axs[0, 1].set_title('IMC vs Expectativa de Vida')
# 3. Magreza (1 a 19 anos)
sns.regplot(data=df, x='thinness1-19years', y='Lifeexpectancy', ax=axs[1, 0], scatter_kws={'alpha': 0.5}, line_kws={'color': 'blue'})
axs[1, 0].set_title('Magreza (1-19 anos) vs Expectativa de Vida')
# 4. HIV/AIDS (como estilo de vida e saúde pública)
sns.regplot(data=df, x='HIV/AIDS', y='Lifeexpectancy', ax=axs[1, 1], scatter_kws={'alpha': 0.5}, line_kws={'color': 'purple'})
axs[1, 1].set_title('HIV/AIDS vs Expectativa de Vida')
st.pyplot(fig)
#----------------------------------------------------
#Qual é o impacto da escolaridade na expectativa de vida dos seres humanos?
st.subheader("Impacto da Escolaridade na Expectativa de Vida", divider=True)
fig, ax = plt.subplots(figsize=(20, 10))
sns.regplot(data=df, x='Schooling', y='Lifeexpectancy', scatter_kws={'alpha': 0.5}, line_kws={'color': 'red'}, ax=ax)
ax.set_title('Escolaridade vs Expectativa de Vida')
ax.set_xlabel('Escolaridade Média (anos)')
ax.set_ylabel('Expectativa de Vida')
st.pyplot(fig)
#----------------------------------------------------
#A expectativa de vida tem relação positiva ou negativa com o consumo de álcool?
st.subheader("Relação entre Consumo de Álcool e Expectativa de Vida", divider=True)

fig, ax = plt.subplots(figsize=(20, 10))
sns.regplot(data=df, x='Alcohol', y='Lifeexpectancy', scatter_kws={'alpha': 0.4}, line_kws={'color': 'red'}, ax=ax)
ax.set_title('Consumo de Álcool vs Expectativa de Vida')
ax.set_xlabel('Consumo de Álcool (litros per capita)')
ax.set_ylabel('Expectativa de Vida')

st.pyplot(fig)
#---------------------------------------------------
#Países densamente povoados tendem a ter menor expectativa de vida?

st.subheader("População Total vs Expectativa de Vida", divider=True)

# Remover valores faltantes
df_plot = df[['Population', 'Lifeexpectancy']].dropna()

fig, ax = plt.subplots(figsize=(20, 10))
sns.scatterplot(data=df_plot, x='Population', y='Lifeexpectancy', alpha=0.6, ax=ax)
ax.set_xscale('log')  # Escala log para melhor visualização
ax.set_title('População Total vs Expectativa de Vida')
ax.set_xlabel('População (escala log)')
ax.set_ylabel('Expectativa de Vida')

st.pyplot(fig)

# Mostrar correlação
st.write("Correlação entre População e Expectativa de Vida:")
st.write(df_plot.corr())
#----------------------------------------------------
#Qual é o impacto da cobertura de imunização na expectativa de vida?
st.subheader("Impacto da Imunização na Expectativa de Vida", divider=True)

vacinas = ['HepatitisB', 'Polio', 'Diphtheria']
for vacina in vacinas:
    dados = df[[vacina, 'Lifeexpectancy']].dropna()

    fig, ax = plt.subplots(figsize=(20, 10))
    sns.regplot(data=dados, x=vacina, y='Lifeexpectancy', scatter_kws={'alpha':0.4}, line_kws={'color':'red'}, ax=ax)
    ax.set_title(f'{vacina} vs Expectativa de Vida')
    ax.set_xlabel(f'Cobertura Vacinal (%) - {vacina}')
    ax.set_ylabel('Expectativa de Vida')
    st.pyplot(fig)

    correlacao = dados.corr().iloc[0,1]
    st.write(f"Correlação entre {vacina} e expectativa de vida: **{correlacao:.2f}**")










