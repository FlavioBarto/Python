import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ---------- Carregar os dados ----------
df = pd.read_csv('dados_vendas_acai.csv', sep=',', encoding='utf-8')

# Converter a coluna de data para datetime
df['data_venda'] = pd.to_datetime(df['data_venda'])

# ---------- Barra lateral - Filtros ----------
st.sidebar.header("Filtros")

# Filtro de data
data_min = df['data_venda'].min().date()
data_max = df['data_venda'].max().date()

data_inicio = st.sidebar.date_input("Data inicial", data_min, min_value=data_min, max_value=data_max)
data_fim = st.sidebar.date_input("Data final", data_max, min_value=data_min, max_value=data_max)

# Filtro de forma de pagamento
formas_pagamento = st.sidebar.multiselect("Forma de pagamento", df['forma_pagamento'].unique(), default=df['forma_pagamento'].unique())

# Filtro de cliente
clientes = st.sidebar.multiselect("Cliente", df['cliente'].unique(), default=df['cliente'].unique())

# ---------- Aplicar filtros ----------
df_filtrado = df[
    (df['data_venda'].dt.date >= data_inicio) &
    (df['data_venda'].dt.date <= data_fim) &
    (df['forma_pagamento'].isin(formas_pagamento)) &
    (df['cliente'].isin(clientes))
]

# ---------- Indicadores ----------
st.title("Dashboard de Vendas")

col1, col2, col3 = st.columns(3)

with col1:
    total_vendas = df_filtrado['valor_total'].sum()
    st.metric("Total de Vendas (R$)", f"{total_vendas:,.2f}")

with col2:
    if len(df_filtrado) > 0:
        ticket_medio = df_filtrado['valor_total'].mean()
    else:
        ticket_medio = 0
    st.metric("Ticket Médio (R$)", f"{ticket_medio:,.2f}")

with col3:
    total_quantidade = df_filtrado['quantidade'].sum()
    st.metric("Qtd. Vendida", int(total_quantidade))

# ---------- Gráfico de Evolução das Vendas ----------
st.subheader("Evolução das Vendas por Dia")

vendas_por_dia = df_filtrado.groupby(df_filtrado['data_venda'].dt.date)['valor_total'].sum()

fig, ax = plt.subplots()
vendas_por_dia.plot(kind='line', marker='o', ax=ax)
ax.set_xlabel("Data")
ax.set_ylabel("Total de Vendas (R$)")
ax.set_title("Evolução Diária das Vendas")
plt.xticks(rotation=45)

st.pyplot(fig)
