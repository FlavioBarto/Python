import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

df = pd.read_csv('dados_vendas_acai.csv', sep=',', encoding='utf-8')

# Estilo personalizado com paleta de cores fornecida
st.markdown("""
<style>
/* Fundo geral */
.body {
    background-color: #f8df82;
}

/* Títulos */
h1, h2, h3, h4 {
    color: #f1ffcf;
    font-family: 'Segoe UI', sans-serif;
}

/* Botões */
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

/* Métricas */
[data-testid="stMetric"] {
    background-color: #9cd6c8;
    color: black;
    padding: 15px;
    border-radius: 12px;
    font-size: 18px;
    font-weight: bold;
}

/* Subtítulos com linha */
.block-container h2 {
    color: #f1ffcf;
    font-size: 24px;
    border-bottom: 3px solid #fac055;
    padding-bottom: 6px;
    margin-bottom: 20px;
}

/* Tabelas */
table {
    border-radius: 12px;
    border: 1px solid #DDD;
}
thead {
    background-color: #fac055;
    color: black;
}
tbody tr:nth-child(even) {
    background-color: #fffdf2;
}
tbody tr:hover {
    background-color: #f8df82;
}

/* Sidebar widgets */
.css-1lcbmhc.e1fqkh3o3 {
    color: #705348;
    font-weight: bold;
}
.css-1y4p8pa.e1fqkh3o6 {
    background-color: #f1ffcf;
}

/* Ocultar rodapé */
footer {
    visibility: hidden;
}
            
.nomedocss {
    padding: 25px;
    background: #9cd6c8;
    width: 400px;
    height: 200px;
}
.EX {
    color: #f1ffcf; 
    font-size: 24px; /* Adicionado para aumentar o tamanho do texto */    
    }
</style>
""", unsafe_allow_html=True)


# Aplicar paleta do seaborn
sns.set_palette(["#9cd6c8", "#f1ffcf", "#f8df82", "#fac055", "#e57c3a", "#705348"])

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
st.markdown(f"""
        <h2>💰 Total de Vendas</h2>
""", unsafe_allow_html = True)
totalvendas = df_filtrado.groupby(df_filtrado['data_venda'].dt.date)['valor_total'].sum()
fig, ax = plt.subplots(figsize=(20, 10))
totalvendas.plot(kind='line', marker='o', ax=ax)
ax.set_xlabel("Data")
ax.set_ylabel("Total de Vendas (R$)")
ax.set_title("Evolução Diária das Vendas")
plt.xticks(rotation=45)
st.pyplot(fig)

#Produtos mais vendidos (Top 5 ou Top 10)
st.markdown(f"""
        <h2>🍰 Top 5 Produtos mais vendidos</h2>
""", unsafe_allow_html = True)

top5 = df_filtrado.groupby('produto')['quantidade'].sum().sort_values(ascending=False).head(5)
fig, ax = plt.subplots()
ax.pie(top5, labels=top5.index, autopct='%1.1f%%', startangle=90)
ax.set_title("Top 5 Produtos Mais Vendidos")
st.pyplot(fig)

#Categorias mais lucrativas somatório de valor_total por categoria

st.subheader("🍰 Categorias mais lucrativas", divider=True)
fig, ax = plt.subplots(figsize=(20, 5))
sns.countplot(data=df_filtrado, x ='valor_total', hue='categoria', ax=ax)
st.pyplot(fig)

#Gráficos de vendas por categoria e produto
st.subheader("📈 Gráficos de vendas por categoria e produto", divider=True)
fig, ax = plt.subplots(figsize=(20, 10))
sns.barplot(data=df_filtrado, x ='produto', y='valor_total', hue='categoria', ax=ax)
st.pyplot(fig)

#Vendas por hora do dia
st.subheader("⏰ Vendas por hora do dia", divider=True)
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
st.subheader("🗓️ Vendas por dia da semana", divider=True)
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


if len(df_filtrado) > 0:
    ticket_medio_pagamento = ticket_medio.mean()
else:
    ticket_medio_pagamento = 0

st.subheader("🧾 Ticket médio por forma de pagamento", divider=True)
st.write("🧾 Ticket Médio", f"R$ {ticket_medio_pagamento:.2f}")

#Clientes que mais compram (Top clientes)
st.subheader("💸 Clientes que mais compram", divider=True)

clientesBons = df_filtrado.groupby('cliente')['quantidade'].sum()
clientesBons = clientesBons.sort_values(ascending=False).head(5)

st.write("Top 5 clientes")
st.dataframe(clientesBons)

#Ticket médio por cliente → média de valor_total agrupada por cliente
st.subheader("📝 Ticket médio por cliente", divider=True)

ticketmediocliente = df_filtrado.groupby('cliente')['valor_total'].sum().sort_values(ascending=False)

st.write("🧾 Ticket Médio por Cliente (média geral):", f"R$ {ticketmediocliente.mean():.2f}")
st.write("📋 Total gasto por cliente:")
st.dataframe(ticketmediocliente)

#Comparativo entre formas de pagamento (volume e valor) → útil para entender preferências e taxas (ex: Pix vs Cartão)

st.subheader("🧾 Comparativo entre formas de pagamento", divider=True)
# Agrupa por forma de pagamento
comparativo_pagamento = df_filtrado.groupby('forma_pagamento').agg({
    'valor_total': ['count', 'sum']
})
# Renomeia as colunas para facilitar leitura
comparativo_pagamento.columns = ['Volume de Vendas', 'Valor Total']
comparativo_pagamento = comparativo_pagamento.sort_values(by='Valor Total', ascending=False)
# Mostra a tabela
st.write("💳 **Comparativo entre Formas de Pagamento**")
st.dataframe(comparativo_pagamento)

metodos_totais = df.groupby('forma_pagamento')['quantidade'].sum()
fig, ax = plt.subplots()
ax.pie(metodos_totais, labels=metodos_totais.index, autopct='%1.1f%%', startangle=90)
ax.set_title("Porcentagem de dos tipos de pagamentos")
st.pyplot(fig)

#Comparação mês a mês ou semana a semana → barras lado a lado: vendas de Maio vs Abril, por exemplo
st.subheader("📊 Comparação mês a mês", divider=True)

df_filtrado['ano_mes'] = df_filtrado['data_venda'].dt.to_period('M').astype(str)
resumoMensal = df_filtrado.groupby('ano_mes')['valor_total'].sum().reset_index()
resumoMensal.columns = ['Mês', 'Total de Vendas']

st.write("📅 Evolução Mensal das Vendas")
st.dataframe(resumoMensal)

st.subheader("🍰 Categorias mais lucrativas", divider=True)
fig, ax = plt.subplots(figsize=(15, 10))
resumoMensal.plot(kind='line', marker='o', ax=ax)
ax.set_xlabel("Mês")
ax.set_ylabel("Total de Vendas (R$)")
ax.set_title("Evolução mensal das Vendas")
st.pyplot(fig)

#Ano anterior x ano atual (YoY) → se houver dados de mais de um ano
st.subheader("🍰 Categorias mais lucrativas", divider=True)
st.write("Não tem vendas de outros anos")

st.subheader("🍰 Categorias mais lucrativas", divider=True)
# Converter datas se necessário
df['data_venda'] = pd.to_datetime(df['data_venda'])
# Lista de produtos únicos
produtos = df['produto'].unique()
produto_selecionado = st.selectbox("Selecione um produto:", produtos)
# Filtrar e agrupar por mês
df_produto = df[df['produto'] == produto_selecionado]
df_evolucao = df_produto.resample('M', on='data_venda').sum(numeric_only=True)
# Mostrar gráfico
st.line_chart(df_evolucao['valor_total'])

#Tabela dinâmica com agrupamentos por cliente, categoria, mês
st.subheader("🍰 Categorias mais lucrativas", divider=True)
# Criar coluna de mês
df['mes'] = df['data_venda'].dt.to_period('M')
# Agrupar
tabela_dinamica = df.groupby(['cliente', 'categoria', 'mes'])['valor_total'].sum().reset_index()
# Mostrar
st.dataframe(tabela_dinamica)

#Número total de clientes únicos
st.subheader("🍰 Categorias mais lucrativas", divider=True)
clientes_unicos = df['cliente'].nunique()
st.metric("Clientes únicos", clientes_unicos)

#Produto mais vendido em quantidade
st.subheader("🍰 Categorias mais lucrativas", divider=True)
produto_mais_vendido = df.groupby('produto')['quantidade'].sum().idxmax()
qtd_mais_vendido = df.groupby('produto')['quantidade'].sum().max()

st.metric("Produto mais vendido", produto_mais_vendido, f"{qtd_mais_vendido} unidades")

#Produto mais lucrativo
st.subheader("🍰 Categorias mais lucrativas", divider=True)
produto_mais_lucrativo = df.groupby('produto')['valor_total'].sum().idxmax()
lucro = df.groupby('produto')['valor_total'].sum().max()

st.metric("Produto mais lucrativo", produto_mais_lucrativo, f"R$ {lucro:,.2f}")

#Valor médio por categoria
st.subheader("🍰 Categorias mais lucrativas", divider=True)
media_categoria = df.groupby('categoria')['valor_total'].mean().reset_index()
st.dataframe(media_categoria)

#Total de vendas no mês atual vs mês anterior (com variação %)
st.subheader("🍰 Categorias mais lucrativas", divider=True)
df['mes'] = df['data_venda'].dt.to_period('M')
mes_atual = df['mes'].max()
mes_anterior = mes_atual - 1

vendas_atual = df[df['mes'] == mes_atual]['valor_total'].sum()
vendas_anterior = df[df['mes'] == mes_anterior]['valor_total'].sum()

variacao = ((vendas_atual - vendas_anterior) / vendas_anterior) * 100 if vendas_anterior != 0 else 0

st.metric("Vendas mês atual", f"R$ {vendas_atual:,.2f}", f"{variacao:.2f}%")





