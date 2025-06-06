import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Carregando os dados
df = pd.read_csv('dados_vendas_acai.csv', sep=',', encoding='utf-8')
df['data_venda'] = pd.to_datetime(df['data_venda'])

# Paleta de cores personalizada
palette = ["#9cd6c8", "#f1ffcf", "#f8df82", "#fac055", "#e57c3a", "#705348"]
sns.set_palette(palette)

# Estilo CSS
st.markdown("""
<style>
body { background-color: #f8df82; }
h1, h2, h3, h4 {
    color: #f1ffcf;
    font-family: 'Segoe UI', sans-serif;
}
.stButton > button {
    background-color: #e57c3a;
    color: white;
    border: none;
    border-radius: 10px;
    padding: 10px 20px;
    font-weight: bold;
    transition: background-color 0.3s ease;
}
.stButton > button:hover {
    background-color: #fac055;
    color: black;
}
[data-testid="stMetric"] {
    background-color: #9cd6c8;
    color: black;
    padding: 15px;
    border-radius: 12px;
    font-size: 18px;
    font-weight: bold;
}
.block-container h2 {
    color: #f1ffcf;
    font-size: 24px;
    border-bottom: 3px solid #fac055;
    padding-bottom: 6px;
    margin-bottom: 20px;
}
table {
    border-radius: 12px;
    border: 1px solid #DDD;
}
thead { background-color: #fac055; color: black; }
tbody tr:nth-child(even) { background-color: #fffdf2; }
tbody tr:hover { background-color: #f8df82; }
footer { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# Filtros no sidebar
data_inicial = st.sidebar.date_input("Data inicial", df['data_venda'].min().date())
data_final = st.sidebar.date_input("Data final", df['data_venda'].max().date())
formas_pagamento = st.sidebar.multiselect("Forma de pagamento", df['forma_pagamento'].unique(), default=df['forma_pagamento'].unique())
clientes = st.sidebar.multiselect("Cliente", df['cliente'].unique(), default=df['cliente'].unique())
produto = st.sidebar.multiselect("Produtos", df['produto'].unique(), default=df['produto'].unique())

# Aplicar filtros
df_filtrado = df[
    (df['data_venda'].dt.date >= data_inicial) &
    (df['data_venda'].dt.date <= data_final) &
    (df['forma_pagamento'].isin(formas_pagamento)) &
    (df['cliente'].isin(clientes)) &
    (df['produto'].isin(produto))
]

# Métricas principais
total_vendas = df_filtrado['valor_total'].sum()
ticket_medio = df_filtrado['valor_total'].mean() if len(df_filtrado) > 0 else 0
quantidade_total = df_filtrado['quantidade'].sum()

col1, col2, col3 = st.columns(3)
col1.metric("\U0001F4B0 Total de Vendas", f"R$ {total_vendas:.2f}")
col2.metric("\U0001F9FE Ticket Médio", f"R$ {ticket_medio:.2f}")
col3.metric("\U0001F4E6 Quantidade Vendida", int(quantidade_total))

# Evolução diária das vendas
st.subheader("\U0001F4B0 Evolução Diária das Vendas")
totalvendas = df_filtrado.groupby(df_filtrado['data_venda'].dt.date)['valor_total'].sum()
fig, ax = plt.subplots(figsize=(20, 10))
totalvendas.plot(kind='line', marker='o', ax=ax)
ax.set_title("Evolução Diária das Vendas")
plt.xticks(rotation=45)
st.pyplot(fig)

# Top 5 produtos mais vendidos
st.subheader("\U0001F370 Top 5 Produtos Mais Vendidos")
top5 = df_filtrado.groupby('produto')['quantidade'].sum().sort_values(ascending=False).head(5)
fig, ax = plt.subplots()
ax.pie(top5, labels=top5.index, autopct='%1.1f%%', startangle=90)
ax.set_title("Top 5 Produtos Mais Vendidos")
st.pyplot(fig)

# Vendas por hora
df_filtrado['hora'] = df_filtrado['data_venda'].dt.hour
vendas_hora = df_filtrado.groupby('hora')['valor_total'].sum().reset_index()
st.subheader("⏰ Vendas por Hora do Dia")
fig, ax = plt.subplots(figsize=(15, 6))
sns.barplot(data=vendas_hora, x='hora', y='valor_total', ax=ax, color='purple')
ax.set_title('Vendas por Hora do Dia')
st.pyplot(fig)

# Vendas por dia da semana
df_filtrado['dia_semana'] = df_filtrado['data_venda'].dt.day_name()
vendas_semana = df_filtrado.groupby('dia_semana')['valor_total'].sum().reset_index()
ordem_dias = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
vendas_semana['dia_semana'] = pd.Categorical(vendas_semana['dia_semana'], categories=ordem_dias, ordered=True)
vendas_semana = vendas_semana.sort_values('dia_semana')

st.subheader("\U0001F4C5 Vendas por Dia da Semana")
fig, ax = plt.subplots(figsize=(15, 6))
sns.barplot(data=vendas_semana, x='dia_semana', y='valor_total', ax=ax, palette='viridis')
ax.set_title("Vendas por Dia da Semana")
st.pyplot(fig)

# Comparativo formas de pagamento
comparativo = df_filtrado.groupby('forma_pagamento').agg({'valor_total': ['count', 'sum']})
comparativo.columns = ['Volume de Vendas', 'Valor Total']
comparativo = comparativo.sort_values(by='Valor Total', ascending=False)

st.subheader("\U0001F9FE Comparativo por Forma de Pagamento")
st.dataframe(comparativo)

# Vendas por mês
df_filtrado['ano_mes'] = df_filtrado['data_venda'].dt.to_period('M').astype(str)
resumoMensal = df_filtrado.groupby('ano_mes')['valor_total'].sum().reset_index()
resumoMensal.columns = ['Mês', 'Total de Vendas']
st.subheader("\U0001F4C6 Vendas Mensais")
st.line_chart(resumoMensal.set_index('Mês'))

# Produto mais vendido
produto_mais_vendido = df.groupby('produto')['quantidade'].sum().idxmax()
qtd_mais_vendido = df.groupby('produto')['quantidade'].sum().max()
st.metric("Produto Mais Vendido", produto_mais_vendido, f"{qtd_mais_vendido} unidades")
