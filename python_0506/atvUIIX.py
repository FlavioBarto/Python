# 📦 Importação de bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# 🗂️ Leitura dos dados
df = pd.read_csv('dados_vendas_acai.csv', sep=',', encoding='utf-8')
df['data_venda'] = pd.to_datetime(df['data_venda'])  # conversão de data

# 🎨 Estilo personalizado
st.markdown("""
<style>
/* Estilização do Streamlit com a paleta personalizada */
body { background-color: #f8df82; }
h1, h2, h3, h4 { color: #f1ffcf; font-family: 'Segoe UI', sans-serif; }
.stButton > button {
    background-color: #e57c3a; color: white; border-radius: 10px;
    padding: 10px 20px; font-weight: bold;
}
.stButton > button:hover { background-color: #fac055; color: black; }
[data-testid="stMetric"] {
    background-color: #9cd6c8; color: black;
    padding: 15px; border-radius: 12px; font-size: 18px; font-weight: bold;
}
.block-container h2 {
    color: #f1ffcf; font-size: 24px;
    border-bottom: 3px solid #fac055; padding-bottom: 6px; margin-bottom: 20px;
}
footer { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

sns.set_palette(["#9cd6c8", "#f1ffcf", "#f8df82", "#fac055", "#e57c3a", "#705348"])

# 🎛️ Filtros no Sidebar
st.sidebar.header("Filtros")
data_inicial = st.sidebar.date_input("Data inicial", df['data_venda'].min().date())
data_final = st.sidebar.date_input("Data final", df['data_venda'].max().date())

formas_pagamento = st.sidebar.multiselect("Forma de pagamento", options=df['forma_pagamento'].unique(), default=df['forma_pagamento'].unique())
clientes = st.sidebar.multiselect("Cliente", options=df['cliente'].unique(), default=df['cliente'].unique())
produto = st.sidebar.multiselect("Produtos", options=df['produto'].unique(), default=df['produto'].unique())

# 🔍 Filtragem de dados
df_filtrado = df[
    (df['data_venda'].dt.date >= data_inicial) &
    (df['data_venda'].dt.date <= data_final) &
    (df['forma_pagamento'].isin(formas_pagamento)) &
    (df['cliente'].isin(clientes)) &
    (df['produto'].isin(produto))
]

# 📊 Métricas principais
total_vendas = df_filtrado['valor_total'].sum()
ticket_medio = df_filtrado['valor_total'].mean() if len(df_filtrado) > 0 else 0
quantidade_total = df_filtrado['quantidade'].sum()

col1, col2, col3 = st.columns(3)
col1.metric("💰 Total de Vendas", f"R$ {total_vendas:.2f}")
col2.metric("🧾 Ticket Médio", f"R$ {ticket_medio:.2f}")
col3.metric("📦 Quantidade Vendida", int(quantidade_total))

# 📈 Evolução diária das vendas
st.markdown("## 💰 Evolução Diária das Vendas")
vendas_diarias = df_filtrado.groupby(df_filtrado['data_venda'].dt.date)['valor_total'].sum()
fig, ax = plt.subplots(figsize=(20, 10))
vendas_diarias.plot(kind='line', marker='o', ax=ax)
ax.set_xlabel("Data")
ax.set_ylabel("Total de Vendas (R$)")
plt.xticks(rotation=45)
st.pyplot(fig)

# 🍰 Top 5 produtos mais vendidos
st.markdown("## 🍰 Top 5 Produtos mais vendidos")
top5 = df_filtrado.groupby('produto')['quantidade'].sum().sort_values(ascending=False).head(5)
fig, ax = plt.subplots()
ax.pie(top5, labels=top5.index, autopct='%1.1f%%', startangle=90)
ax.set_title("Top 5 Produtos Mais Vendidos")
st.pyplot(fig)

# 📊 Vendas por categoria
st.subheader("🍰 Categorias mais lucrativas")
fig, ax = plt.subplots(figsize=(20, 5))
sns.countplot(data=df_filtrado, x='valor_total', hue='categoria', ax=ax)
st.pyplot(fig)

# 📊 Vendas por produto e categoria
st.subheader("📈 Vendas por categoria e produto")
fig, ax = plt.subplots(figsize=(20, 10))
sns.barplot(data=df_filtrado, x='produto', y='valor_total', hue='categoria', ax=ax)
st.pyplot(fig)

# 🕒 Vendas por hora do dia
st.subheader("⏰ Vendas por hora do dia")
df_filtrado['hora'] = df_filtrado['data_venda'].dt.hour
vendas_hora = df_filtrado.groupby('hora')['valor_total'].sum().reset_index()
fig, ax = plt.subplots(figsize=(15, 6))
sns.barplot(data=vendas_hora, x='hora', y='valor_total', color='purple', ax=ax)
st.pyplot(fig)

# 📆 Vendas por dia da semana
st.subheader("🗓️ Vendas por dia da semana")
df_filtrado['dia_semana'] = df_filtrado['data_venda'].dt.day_name()
vendas_dia = df_filtrado.groupby('dia_semana')['valor_total'].sum().reset_index()
ordem_dias = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
vendas_dia['dia_semana'] = pd.Categorical(vendas_dia['dia_semana'], categories=ordem_dias, ordered=True)
vendas_dia = vendas_dia.sort_values('dia_semana')
fig, ax = plt.subplots(figsize=(15, 6))
sns.barplot(data=vendas_dia, x='dia_semana', y='valor_total', palette='viridis', ax=ax)
st.pyplot(fig)

# 💳 Ticket médio por forma de pagamento
st.subheader("🧾 Ticket médio por forma de pagamento")
ticket_pagamento = df_filtrado.groupby('forma_pagamento')['valor_total'].mean().reset_index()
st.dataframe(ticket_pagamento)

# 👥 Top clientes por quantidade
st.subheader("💸 Clientes que mais compram")
top_clientes = df_filtrado.groupby('cliente')['quantidade'].sum().sort_values(ascending=False).head(5)
st.dataframe(top_clientes)

# 📝 Ticket médio por cliente
st.subheader("📝 Ticket médio por cliente")
ticket_cliente = df_filtrado.groupby('cliente')['valor_total'].sum().sort_values(ascending=False)
st.write("🧾 Ticket Médio Geral:", f"R$ {ticket_cliente.mean():.2f}")
st.dataframe(ticket_cliente)

# 📊 Comparativo entre formas de pagamento
st.subheader("🧾 Comparativo entre formas de pagamento")
comparativo = df_filtrado.groupby('forma_pagamento').agg({'valor_total': ['count', 'sum']})
comparativo.columns = ['Volume de Vendas', 'Valor Total']
st.dataframe(comparativo)

metodos_totais = df['forma_pagamento'].value_counts()
fig, ax = plt.subplots()
ax.pie(metodos_totais, labels=metodos_totais.index, autopct='%1.1f%%', startangle=90)
st.pyplot(fig)

# 📅 Comparação mês a mês
st.subheader("📊 Comparação mês a mês")
df_filtrado['ano_mes'] = df_filtrado['data_venda'].dt.to_period('M').astype(str)
resumo_mensal = df_filtrado.groupby('ano_mes')['valor_total'].sum().reset_index()
resumo_mensal.columns = ['Mês', 'Total de Vendas']
st.line_chart(resumo_mensal.set_index('Mês'))

# 📌 Evolução de produto específico
st.subheader("📈 Evolução de um produto específico")
produto_sel = st.selectbox("Selecione um produto:", df['produto'].unique())
df_produto = df[df['produto'] == produto_sel]
evolucao = df_produto.resample('M', on='data_venda')['valor_total'].sum()
st.line_chart(evolucao)

# 🧮 Tabela dinâmica por cliente, categoria e mês
st.subheader("📊 Tabela dinâmica por cliente/categoria/mês")
df['mes'] = df['data_venda'].dt.to_period('M')
tabela_dinamica = df.groupby(['cliente', 'categoria', 'mes'])['valor_total'].sum().reset_index()
st.dataframe(tabela_dinamica)

# 🔢 Clientes únicos
st.subheader("👥 Total de clientes únicos")
clientes_unicos = df['cliente'].nunique()
st.metric("Clientes únicos", clientes_unicos)

# 🥇 Produto mais vendido
st.subheader("🏆 Produto mais vendido")
produto_top = df.groupby('produto')['quantidade'].sum().idxmax()
qtd_top = df.groupby('produto')['quantidade'].sum().max()
st.metric("Produto mais vendido", produto_top, f"{qtd_top} unidades")

# 💼 Produto mais lucrativo
st.subheader("💸 Produto mais lucrativo")
produto_lucrativo = df.groupby('produto')['valor_total'].sum().idxmax()
lucro = df.groupby('produto')['valor_total'].sum().max()
st.metric("Produto mais lucrativo", produto_lucrativo, f"R$ {lucro:,.2f}")

# 📚 Valor médio por categoria
st.subheader("📊 Valor médio por categoria")
media_categoria = df.groupby('categoria')['valor_total'].mean().reset_index()
st.dataframe(media_categoria)

st.subheader("📅 Comparativo mês atual vs anterior")
mes_atual = df['mes'].max()
mes_anterior = mes_atual - 1
vendas_atual = df[df['mes'] == mes_atual]['valor_total'].sum()
vendas_ant = df[df['mes'] == mes_anterior]['valor_total'].sum()
variacao = ((vendas_atual - vendas_ant) / vendas_ant * 100) if vendas_ant != 0 else 0
st.metric("Vendas mês atual", f"R$ {vendas_atual:,.2f}", f"{variacao:.2f}%")
