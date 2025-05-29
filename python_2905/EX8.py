import sqlite3
import pandas as pd
import streamlit as st

#Criando a bilioteca:
conn = sqlite3.connect("Bilioteca.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS autores(
    id INTEGER AUTO INCREMENT,
    nome VARCHAR(150) NOT NULL, 
        PRIMARY KEY (id)
               )
''')
cursor.execute('''
CREATE TABLE IF NOT EXIST categorias(
    id INTEGER AUTO INCREMENT,
    nome VARCHAR(150) NOT NULL,  
        PRIMARY KEY (id)         
               )
''')
cursor.execute('''
CREATE TABLE IF NOT EXIST livros(
    id INTEGER AUTOINCREMENT,
    titulo VARCHAR(150) NOT NULL,
    autor_id INTEGER NOT NULL,
    categoria_id INTEGER NOT NULL,
    ano DATE NOT NULL,
    qtdDisponivel  INTEGER NOT NULL, 
    PRIMARY KEY(id),
        FOREIGN KEY (autor_id), 
        REFERENCES autores (id),  
        FOREIGN KEY (categoria_id), 
        REFERENCES categorias (id) 
    )
''')
cursor.execute('''
CREATE TABLE IF NOT EXIST emprestimos(
    id INTEGER AUTO INCREMENT,
    livro_id INTEGER FOREIGN KEY,
    data_emp DATE NOT NULL,
    devolvido BOOLEAN NOT NULL,
        PRIMARY KEY(id),
            FOREIGN KEY(livro_id),
            REFERENCE livros (id)   
    )
''')
conn.commit()

cursor.execute("SELECT COUNT(*) FROM autores")
if cursor.fetchone()[0] == 0:
    autores_iniciais = [
        ('Machado de Assis'),
        ('CS Lewis'),

    ]
    cursor.executemany("INSERT INTO autores (nome) VALUES (?)", autores_iniciais)
    conn.commit()

st.title("teste")
st.subheader("📋 Tabela: SELECT * FROM autores")
df = pd.read_sql_query("SELECT * FROM autores", conn)
st.dataframe(df)