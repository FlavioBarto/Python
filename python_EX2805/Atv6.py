
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

df = pd.read_csv('clientes.csv', sep=',', encoding='latin1')
df.columns = [col.strip().replace('�','a').replace('ã','a').replace('ç','c').replace('á','a').replace(' ', '') for col in df.columns]
st.write(df.columns)

df['cancelados'] = df['Categoria'] == 'Cancelado'
st.subheader(f"total de cancelados", divider=True)
st.write(f"canselados: {df['cancelados'].sum()}")
#-------------------------------------------------------------
st.subheader("Cancelamento por Genero", divider=True)
fig1, ax1 = plt.subplots(figsize=(30, 15))
sns.countplot(x='Sexo', hue='Categoria', ax=ax1, data=df)
st.pyplot(fig1)

st.subheader("Cancelamentos por Salario", divider=True)
fig2, ax2 = plt.subplots(figsize=(30, 15))
sns.countplot(x='FaixaSalarialAnual', hue='Categoria', order= df['FaixaSalarialAnual'].value_counts().index, ax=ax2, data=df)
st.pyplot(fig2)

st.subheader("Distribuição de Limite", divider=True)
fig3, ax3 = plt.subplots(figsize=(30, 15))
sns.histplot(data=df, y='LimiteDisponível', hue='Categoria', kde=True, ax=ax3)
st.pyplot(fig3)

st.subheader("Relação entre Inatividade e Cancelamento", divider=True)
fig4, ax4 = plt.subplots(figsize=(30, 15))
sns.countplot(data=df, x ='Inatividade12m', hue='Categoria', ax=ax4)
st.pyplot(fig4)

st.subheader("Conclusão da analise", divider=True)
st.write("Pelo que podemos ver nos graficos as pessoas com baixo limite, renda baixa ou que não usam a mais de 2 meses o cartão tendem a cancelar o mesmo")





