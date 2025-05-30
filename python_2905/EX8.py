import sqlite3
import pandas as pd
import streamlit as st

# Criando a conexão
with sqlite3.connect("Biblioteca.db", check_same_thread=False) as conn:
    cursor = conn.cursor()

# Tabela de autores
cursor.execute('''
CREATE TABLE IF NOT EXISTS autores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(150) NOT NULL
)
''')
conn.commit()

# Tabela de categorias
cursor.execute('''
CREATE TABLE IF NOT EXISTS categorias (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(150) NOT NULL
)
''')
conn.commit()

# Tabela de livros
cursor.execute('''
CREATE TABLE IF NOT EXISTS livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo VARCHAR(150) NOT NULL,
    autor_id INTEGER NOT NULL,
    categoria_id INTEGER NOT NULL,
    ano DATE NOT NULL,
    qtdDisponivel INTEGER NOT NULL,
    FOREIGN KEY (autor_id) REFERENCES autores(id),
    FOREIGN KEY (categoria_id) REFERENCES categorias(id)
)
''')
conn.commit()

# Tabela de empréstimos
cursor.execute('''
CREATE TABLE IF NOT EXISTS emprestimos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    livro_id INTEGER NOT NULL,
    data_emp DATE NOT NULL,
    devolvido BOOLEAN NOT NULL,
    FOREIGN KEY (livro_id) REFERENCES livros(id)
)
''')

conn.commit()

# Inserção de autores se ainda não existirem
cursor.execute("SELECT COUNT(*) FROM autores")
if cursor.fetchone()[0] == 0:
    autores_iniciais = [
        ('Machado de Assis',),
        ('CS Lewis',)
    ]
    cursor.executemany("INSERT INTO autores (nome) VALUES (?)", autores_iniciais)
    conn.commit()

# Inserção de categorias se ainda não existirem
cursor.execute("SELECT COUNT(*) FROM categorias")
if cursor.fetchone()[0] == 0:
    Categorias_iniciais = [
        ('Ação',), #0
        ('Suspense',), #1
        ('Romance',), #2
        ('Terror',), #3
        ('Cristão',), #4
        ('Fantasia',), #5
        ('Gibi',), #6
        ('Distopia',) #7
    ]
    cursor.executemany("INSERT INTO categorias (nome) VALUES (?)", Categorias_iniciais)
    conn.commit()

# Inserção de livros se ainda não existirem
cursor.execute("SELECT COUNT(*) FROM livros")
if cursor.fetchone()[0] == 0:
    livros_iniciais = [
        ('titulo1', 0, 2, 2020, 20),
        ('titulo2', 1, 4, 1999, 10),
        ('titulo3', 1, 7, 2025, 30),
    ]
    cursor.executemany("INSERT INTO livros (titulo, autor_id, categoria_id, ano, qtdDisponivel) VALUES (?, ?, ?, ?, ?)", livros_iniciais)
    conn.commit()

#inserir novos livros na biblioteca
#novos_livros = [
   # ('titulo4', 0, 3, 2020, 20),
   # ('titulo5', 1, 4, 1999, 10),
   # ('titulo6', 1, 5, 2025, 30),
   # ('titulo7', 0, 6, 2020, 20),
   # ('titulo8', 1, 1, 1999, 10),
   # ('titulo9', 1, 0, 2025, 30),
   # ('titulo10', 0, 2, 2020, 20),
   # ('titulo11', 1, 4, 1999, 10)
#]

# Inserindo os novos livros
#cursor.executemany(
  #  "INSERT INTO livros (titulo, autor_id, categoria_id, ano, qtdDisponivel) VALUES (?, ?, ?, ?, ?)",
  #  novos_livros
#)
#conn.commit()

# Inserção de empréstimos se ainda não existirem
cursor.execute("SELECT COUNT(*) FROM emprestimos")
if cursor.fetchone()[0] == 0:
    emprestimos_iniciais = [
        ('0','12/02/2020', False),
        ('1','23/04/2017', False)
    ]
    cursor.executemany("INSERT INTO emprestimos (livro_id, data_emp, devolvido) VALUES (?, ?, ?)", emprestimos_iniciais)
    conn.commit()

# Exibir tabela de autores
st.title("teste")
st.subheader("📋 Tabela: SELECT * FROM autores", divider=True)
df = pd.read_sql_query("SELECT * FROM autores", conn)
st.dataframe(df)


st.title("teste")
st.subheader("📋 Tabela: SELECT * FROM categorias", divider=True)
df = pd.read_sql_query("SELECT * FROM categorias", conn)
st.dataframe(df)

st.title("teste")
st.subheader("📋 Tabela: SELECT id FROM livros", divider=True)
df = pd.read_sql_query("SELECT * FROM livros", conn)
st.dataframe(df)

st.title("teste")
st.subheader("📋 Tabela: SELECT * FROM emprestimos", divider=True)
df = pd.read_sql_query("SELECT * FROM emprestimos", conn)
st.dataframe(df)

#Todos os livros com nome do autor e da categoria.

# SELECT com colunas específicas
st.subheader("Todos os livros com nome do autor e da categoria: ", divider=True)
query = """
    SELECT l.titulo AS Titulo, a.nome AS autor, c.nome AS categoria
FROM livros l
JOIN autores a ON l.autor_id = a.id
JOIN categorias c ON l.categoria_id = c.id;
"""
df = pd.read_sql_query(query, conn)
st.dataframe(df)


#Filtro de livros por ano de publicação.
st.subheader("Filtro de livros por ano de publicação: ", divider=True)
df = pd.read_sql_query('''
    SELECT * FROM livros
    ORDER BY ano DESC
''', conn)
st.dataframe(df)

#Quantidade total de livros, de empréstimos e devolvidos.

st.subheader("📊 Quantidade total de livros, empréstimos e devoluções:", divider=True)
df = pd.read_sql_query('''
    SELECT
        (SELECT COUNT(*) FROM livros) AS total_livros,
        (SELECT COUNT(*) FROM emprestimos) AS total_emprestimos,
        (SELECT COUNT(*) FROM emprestimos WHERE devolvido = 1) AS total_devolvidos
''', conn)
st.dataframe(df)


#Número de livros por categoria (agrupado).
st.subheader("📚 Número de livros por categoria:", divider=True)
df = pd.read_sql_query('''
    SELECT categorias.nome AS categoria, COUNT(*) AS total_livros
    FROM livros
    JOIN categorias ON livros.categoria_id = categorias.id
    GROUP BY categorias.nome
''', conn)
st.dataframe(df)


#Formulário para registrar novo empréstimo ou novo livro.
# ➕ Inserir novo produto
st.subheader("➕ Inserir novo Livro", divider=True)

# Buscar autores e categorias do banco
autores = pd.read_sql_query("SELECT id, nome FROM autores", conn)
categorias = pd.read_sql_query("SELECT id, nome FROM categorias", conn)

with st.form("form_inserir"):
    nome = st.text_input("Título: ")
    ano = st.number_input("Ano de publicação:", min_value=1900, max_value=2025, step=1)
    autor_nome = st.selectbox("Autor:", autores["nome"].tolist())
    categoria_nome = st.selectbox("Categoria:", categorias["nome"].tolist())
    qtd = st.number_input("Quantidade disponível:", min_value=1, max_value=30, step=1)

    enviar = st.form_submit_button("Inserir")

    if enviar and nome and ano:
        # Obter o id do autor e da categoria selecionados
        autor_id = autores.loc[autores["nome"] == autor_nome, "id"].values[0]
        categoria_id = categorias.loc[categorias["nome"] == categoria_nome, "id"].values[0]

        # Inserir no banco
        cursor.execute(
            "INSERT INTO livros (titulo, autor_id, categoria_id, ano, qtdDisponivel) VALUES (?, ?, ?, ?, ?)",
            (nome, autor_id, categoria_id, ano, qtd)
        )
        conn.commit()
        st.success(f"Livro '{nome}' inserido com sucesso!")
        st.rerun()

#Formulário para editar um autor (alterar o nome)
st.subheader("Editar Autor: ", divider=True)

with st.form("form_editar_autor"):
    autor_nome = st.selectbox("Autor:", autores["nome"].tolist())
    nome = st.text_input("Troque o nome: ")
    enviar = st.form_submit_button("alterar")

    if enviar and nome and ano:
        # Obter o id do autor e da categoria selecionados

        # Inserir no banco
        cursor.execute(
            "UPDATE autores SET nome = ? WHERE nome = ?",
            (autor_nome ,nome)
        )
        conn.commit()
        st.success(f"Autor '{autor_nome}' alterado com sucesso para '{nome}'!")
        st.rerun()

st.title("teste2")
st.subheader("📋 Tabela: SELECT * FROM autores", divider=True)
df = pd.read_sql_query("SELECT * FROM autores", conn)
st.dataframe(df)
#Formulário para editar um livro (alterar titulo, nome, categoria, quantidade disponivel)
# Formulário para editar um livro
st.subheader("✏️ Editar Livro", divider=True)

livros = pd.read_sql_query("SELECT * FROM livros", conn)

with st.form("form_editar_livro"):
    livro_titulo = st.selectbox("Escolha o livro para editar:", livros["titulo"].tolist())
    
    novo_titulo = st.text_input("Novo título:")
    novo_autor = st.selectbox("Novo autor:", autores["nome"].tolist())
    nova_categoria = st.selectbox("Nova categoria:", categorias["nome"].tolist())
    novo_ano = st.number_input("Novo ano de publicação:", min_value=1900, max_value=2025, step=1)
    nova_qtd = st.number_input("Nova quantidade disponível:", min_value=1, max_value=100, step=1)

    editar = st.form_submit_button("Salvar Alterações")

    if editar and novo_titulo:
        livro_id = livros.loc[livros["titulo"] == livro_titulo, "id"].values[0]
        novo_autor_id = autores.loc[autores["nome"] == novo_autor, "id"].values[0]
        nova_categoria_id = categorias.loc[categorias["nome"] == nova_categoria, "id"].values[0]

        cursor.execute('''
            UPDATE livros
            SET titulo = ?, autor_id = ?, categoria_id = ?, ano = ?, qtdDisponivel = ?
            WHERE id = ?
        ''', (novo_titulo, novo_autor_id, nova_categoria_id, novo_ano, nova_qtd, livro_id))

        conn.commit()
        st.success(f"Livro '{livro_titulo}' atualizado com sucesso!")
        st.rerun()
#Formulário para Deletar um livro ou autor.
# Formulário para deletar um livro ou autor
st.subheader("🗑️ Deletar Livro ou Autor", divider=True)

aba1, aba2 = st.tabs(["Deletar Livro", "Deletar Autor"])

with aba1:
    with st.form("form_deletar_livro"):
        livro_nome = st.selectbox("Escolha o livro para deletar:", livros["titulo"].tolist())
        deletar_livro = st.form_submit_button("Deletar Livro")

        if deletar_livro:
            livro_id = livros.loc[livros["titulo"] == livro_nome, "id"].values[0]
            cursor.execute("DELETE FROM livros WHERE id = ?", (livro_id,))
            conn.commit()
            st.success(f"Livro '{livro_nome}' deletado com sucesso!")
            st.rerun()

with aba2:
    with st.form("form_deletar_autor"):
        autor_nome = st.selectbox("Escolha o autor para deletar:", autores["nome"].tolist())
        deletar_autor = st.form_submit_button("Deletar Autor")

        if deletar_autor:
            autor_id = autores.loc[autores["nome"] == autor_nome, "id"].values[0]
            cursor.execute("DELETE FROM autores WHERE id = ?", (autor_id,))
            conn.commit()
            st.success(f"Autor '{autor_nome}' deletado com sucesso!")
            st.rerun()
