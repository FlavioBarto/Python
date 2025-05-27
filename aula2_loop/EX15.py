#Crie uma lista com notas de alunos e use um loop para classificar cada uma como "Aprovado" (>= 6) ou "Reprovado".

nota = []
for i in range(10):
    nota.append(i)

for i in range(len(nota)):
    if(nota[i] >= 6):
        print("aluno", i+1, "aprovado")
    else:
        print("aluno", i+1, "Reprovado")