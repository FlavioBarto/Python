import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

df = pd.read_csv('Life_Expectancy_Data.csv', sep=',', encoding='latin1')
df.columns = [col.strip().replace('�','a').replace('ã','a').replace('ç','c').replace('á','a').replace(' ', '') for col in df.columns]
st.write(df.columns)

#-----------------------------------------------------
#Os vários fatores de previsão inicialmente escolhidos realmente afetam a expectativa de vida? Quais são as variáveis de previsão que realmente afetam a expectativa de vida?
#imunização (hepatite B, poliomielite, difteria), mortalidade, aspectos econômicos, sociais e de saúde.
st.subheader("Quais são as variaveis que afetam a expectativa de vida", divider=True)
afeganistao = df['Country'] == 'Afghanistan'
afe = df[afeganistao]
afe = afe.sort_values(by='Year', ascending=True)
st.write(afe)

st.subheader("correlações", divider=True)
numeric_df = df.select_dtypes(include=['number'])
correlacao = numeric_df.corr()

fig, ax = plt.subplots(figsize=(30, 15))
sns.heatmap(correlacao, annot=True, cmap="coolwarm")
st.pyplot(fig)



