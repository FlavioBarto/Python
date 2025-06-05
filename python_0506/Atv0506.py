import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

df = pd.read_csv('dados_vendas_acai.csv', sep=',', encoding='utf-8')

# Converter data para datetime
df['data_venda'] = pd.to_datetime(df['data_venda'])


#data inicial e final
data_inicial = st.sidebar.date_input("Data inicial", df['data_venda'].min().date())
data_final = st.sidebar.date_input("Data final", df['data_venda'].max().date())

#filtrar os pagamentos
formas_pagamento = st.sidebar.multiselect(
    "Forma de pagamento",
    options=df['forma_pagamento'].unique(),
    default=df['forma_pagamento'].unique()
)

#filtrar por clientes
clientes = st.sidebar.multiselect(
    "Cliente",
    options=df['cliente'].unique(),
    default=df['cliente'].unique()
)
produto = st.sidebar.multiselect(
    "Produtos: ",
    options=df['produto'].unique(),
    default=df['produto'].unique()
)

df_filtrado = df[
    #Mantém apenas as linhas em que a data da venda é maior ou igual a data_inicial.
    (df['data_venda'].dt.date >= data_inicial) &
    #também onde a data da venda é menor ou igual a data_final.
    (df['data_venda'].dt.date <= data_final) &
    #onde a forma de pagamento está dentro da lista formasPagamento.
    #isin significa esta dentro (is in == esta dentro)
    (df['forma_pagamento'].isin(formas_pagamento)) &
    #onde o cliente está dentro da lista clientes.
    (df['cliente'].isin(clientes)) &
    (df['produto'].isin(produto))
]
#somando o valor total
total_vendas = df_filtrado['valor_total'].sum()



if len(df_filtrado) > 0:
    ticket_medio = df_filtrado['valor_total'].mean()
else:
    ticket_medio = 0

quantidade_total = df_filtrado['quantidade'].sum()
col1, col2, col3 = st.columns(3)

col1.metric("💰 Total de Vendas", f"R$ {total_vendas:.2f}")
col2.metric("🧾 Ticket Médio", f"R$ {ticket_medio:.2f}")
col3.metric("📦 Quantidade Vendida", int(quantidade_total))

#Gráfico com evolução das vendas

totalvendas = df_filtrado.groupby(df_filtrado['data_venda'].dt.date)['valor_total'].sum()

fig, ax = plt.subplots(figsize=(15, 10))
totalvendas.plot(kind='line', marker='o', ax=ax)
ax.set_xlabel("Data")
ax.set_ylabel("Total de Vendas (R$)")
ax.set_title("Evolução Diária das Vendas")
plt.xticks(rotation=45)
st.pyplot(fig)

#Produtos mais vendidos (Top 5 ou Top 10)
top5 = df_filtrado.groupby('produto')['quantidade'].sum().sort_values(ascending=False).head(5)
fig, ax = plt.subplots()
ax.pie(top5, labels=top5.index, autopct='%1.1f%%', startangle=90)
ax.set_title("Top 5 Produtos Mais Vendidos")
st.pyplot(fig)

#Categorias mais lucrativas somatório de valor_total por categoria
fig, ax = plt.subplots(figsize=(20, 10))
sns.countplot(data=df_filtrado, x ='valor_total', hue='categoria', ax=ax)
st.pyplot(fig)

#Gráficos de vendas por categoria e produto
fig, ax = plt.subplots(figsize=(20, 10))
sns.barplot(data=df_filtrado, x ='produto', y='valor_total', hue='categoria', ax=ax)
st.pyplot(fig)

#Vendas por hora do dia
df_filtrado['hora'] = df_filtrado['data_venda'].dt.hour
vendas_hora_valor = df_filtrado.groupby('hora')['valor_total'].sum().reset_index()

# Gráfico de barras
fig, ax = plt.subplots(figsize=(15, 6))
sns.barplot(data=vendas_hora_valor, x='hora', y='valor_total', ax=ax, color='purple')
ax.set_title('Valor Total de Vendas por Hora do Dia')
ax.set_xlabel('Hora do Dia')
ax.set_ylabel('Valor Total (R$)')
plt.xticks(range(0, 24))
st.pyplot(fig)

#Vendas por dia da semana

df_filtrado['dia_semana'] = df_filtrado['data_venda'].dt.day_name()
vendas_porDia = df_filtrado.groupby('dia_semana')['valor_total'].sum().reset_index()
ordem_dias = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
vendas_porDia['dia_semana'] = pd.Categorical(vendas_porDia['dia_semana'], categories=ordem_dias, ordered=True)
vendas_porDia = vendas_porDia.sort_values('dia_semana')

fig, ax = plt.subplots(figsize=(15, 6))
sns.barplot(data=vendas_porDia, x='dia_semana', y='valor_total', ax=ax, palette='viridis')
ax.set_title("Vendas por Dia da Semana")
ax.set_xlabel("Dia da Semana")
ax.set_ylabel("Valor Total de Vendas (R$)")
st.pyplot(fig)

#Ticket médio por forma de pagamento // média do valor_total agrupada por forma_pagamento




