import sqlite3
import pandas as pd
import streamlit as st

# Conecta (ou cria) o banco de dados SQLite
conn = sqlite3.connect("produtos.db")
cursor = conn.cursor()

# Cria a tabela se não existir (DDL)
cursor.execute('''
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL,
    categoria TEXT NOT NULL
)
''')
conn.commit()

# Dados iniciais (DML - inserção se a tabela estiver vazia)
cursor.execute("SELECT COUNT(*) FROM produtos")
if cursor.fetchone()[0] == 0:
    produtos_iniciais = [
        ('Sorvete de Chocolate', 7.5, 'Sobremesa'),
        ('Picolé de Morango', 4.0, 'Sobremesa'),
        ('Água Mineral', 2.0, 'Bebida'),
        ('Refrigerante', 6.0, 'Bebida'),
        ('Café Gelado', 5.0, 'Bebida'),
    ]
    cursor.executemany("INSERT INTO produtos (nome, preco, categoria) VALUES (?, ?, ?)", produtos_iniciais)
    conn.commit()

st.title("🎓 Fundamentos de SQL com Python + Streamlit + SQLite")

# SELECT * FROM produtos
st.subheader("📋 Tabela: SELECT * FROM produtos")
df = pd.read_sql_query("SELECT * FROM produtos", conn)
st.dataframe(df)

# WHERE - filtro de preço
st.subheader("🔍 Filtro: WHERE preco > ...")
valor_min = st.slider("Preço mínimo", 0.0, 10.0, 5.0, 0.5)
df_filtro = pd.read_sql_query("SELECT * FROM produtos WHERE preco > ?", conn, params=(valor_min,))
st.dataframe(df_filtro)

# SELECT com colunas específicas
st.subheader("🧾 SELECT nome, preco")
df_select = pd.read_sql_query("SELECT nome, preco FROM produtos", conn)
st.dataframe(df_select)

# Funções agregadas
st.subheader("📊 Funções agregadas (AVG, SUM, COUNT)")
df_agregado = pd.read_sql_query('''
    SELECT
        ROUND(AVG(preco), 2) AS media,
        ROUND(SUM(preco), 2) AS soma,
        COUNT(*) AS total
    FROM produtos
''', conn)
st.dataframe(df_agregado)

# GROUP BY
st.subheader("📂 GROUP BY categoria")
df_group = pd.read_sql_query('''
    SELECT categoria, COUNT(*) AS total_produtos, ROUND(AVG(preco), 2) AS media_preco
    FROM produtos
    GROUP BY categoria
''', conn)
st.dataframe(df_group)

# Inserção de novo produto
st.subheader("➕ Inserir novo produto")
with st.form("form_inserir"):
    nome = st.text_input("Nome do produto")
    preco = st.number_input("Preço", min_value=0.0, step=0.5)
    categoria = st.selectbox("Categoria", ['Sobremesa', 'Bebida', 'Outros'])
    enviar = st.form_submit_button("Inserir")

    if enviar and nome and preco > 0:
        cursor.execute("INSERT INTO produtos (nome, preco, categoria) VALUES (?, ?, ?)",
                       (nome, preco, categoria))
        conn.commit()
        st.success(f"Produto '{nome}' inserido com sucesso!")
        st.experimental_rerun()

# Fechando conexão
conn.close()
