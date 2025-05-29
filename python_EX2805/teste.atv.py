import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Carregar dados
df = pd.read_csv('Life_Expectancy_Data.csv', sep=',', encoding='latin1')
df.columns = [col.strip().replace('�','a').replace('ã','a').replace('ç','c').replace('á','a').replace(' ', '') for col in df.columns]

# Remover linhas com valores nulos nas colunas críticas
df = df.dropna(subset=['Lifeexpectancy', 'Totalexpenditure'])

# Filtrar apenas o ano de 2015 (último ano disponível)
df_2015 = df[df['Year'] == 2015].copy()

# Criar nova coluna booleana: expectativa de vida >= 65 anos
df_2015['AltaExpectativa'] = df_2015['Lifeexpectancy'] >= 65

# Título
st.title("Análise de Expectativa de Vida e Gastos com Saúde")

# Gráfico comparando gasto com saúde entre os dois grupos
st.subheader("Gasto com saúde vs Expectativa de vida (2015)")

fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(data=df_2015, x='AltaExpectativa', y='Totalexpenditure')
ax.set_xlabel("Expectativa de vida >= 65 anos?")
ax.set_ylabel("Gasto Total com Saúde (% do PIB)")
ax.set_title("Comparação de Gastos com Saúde entre Grupos")
st.pyplot(fig)

# Mostrar médias dos dois grupos
media_alta = df_2015[df_2015['AltaExpectativa']]['Totalexpenditure'].mean()
media_baixa = df_2015[~df_2015['AltaExpectativa']]['Totalexpenditure'].mean()

st.write(f"**Média de gasto com saúde (% do PIB)**")
st.write(f"- Países com expectativa de vida >= 65: `{media_alta:.2f}`")
st.write(f"- Países com expectativa de vida < 65: `{media_baixa:.2f}`")

# Conclusão inicial
if media_baixa < media_alta:
    st.success("Países com menor expectativa de vida tendem a gastar menos com saúde. Pode ser necessário aumentar o investimento.")
else:
    st.warning("Não há diferença clara nos gastos com saúde entre os dois grupos.")
