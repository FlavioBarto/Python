
import pandas as pd
media = 0
grupo = {}

df = pd.read_csv('Pandas/feedbacks.csv')
media = df['nota'].mean()
print(media)
#------------------------------------------------
grupo = df.groupby('curso')['nota'].mean()
melhor = grupo.max()
pior = grupo.min()

Curso_melhor = grupo.idxmax()
Curso_pior = grupo.idxmin()

print(f"melhor: {Curso_melhor}: ({melhor:.2}), pior: {Curso_pior}: ({pior:.2})")
#------------------------------------------------
#conta = df.loc[df.recomendaria == 'sim']
conta = df[df['recomendaria'].str.lower() == 'sim'] #envia um dataframe para o conta que agrupa todos os cursos que recomandaram como sim
recomendacoes = conta['curso'].value_counts()
print(recomendacoes)
#------------------------------------------------
#Ver quantidade de feedbacks por dia
porDia = df.groupby('data').size() #agrupa e soma se a data for a mesma na coluna
print(porDia)
#------------------------------------------------
#Filtrar só os feedbacks negativos (nota <= 2)
negativos = df[df['nota'] <= 2]
feedbacks_negativos = negativos[['data', 'curso', 'nota', 'comentario', 'recomendaria']]
print("esses são negativos: ")
print(feedbacks_negativos)
#------------------------------------------------
#Salvar um relatório feedbacks_negativos.csv
feedbacks_negativos.to_csv('feedbacks_negativos.csv', index=False)

fn = pd.read_csv('feedbacks_negativos.csv')
negativosdodia = fn.groupby('data').size()
        
print(negativosdodia)
