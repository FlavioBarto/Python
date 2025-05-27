import pandas as pd
df = pd.read_csv('Pandas/feedbacks.csv')
media = df['nota'].mean
#print(media)
#------------------------------------------
grupo = df.groupby('curso')['nota'].mean() #Calcula a média das notas de cada grupo (curso).
melhor = grupo.max()
pior = grupo.min()

nomeMelhor = grupo.idxmax()
nomePior = grupo.idxmin()

#print(f"esse é o melhor {nomeMelhor} com {melhor:.2} e esse é o pior {nomePior} com {pior:.2}")
#-----------------------------------------
recom = df[df['recomendaria'].str.lower() == 'sim']
recomenda = recom['curso'].value_counts()
#print(recomenda)
#-----------------------------------------
porDia = df.groupby('data').size()
#print(porDia)
#-----------------------------------------
masrecom = df[df['nota'] <= 2]
feedbacks_negativos = masrecom[['data', 'curso', 'nota', 'comentario', 'recomendaria']]

print(feedbacks_negativos)