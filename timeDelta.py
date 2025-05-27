from datetime import date, datetime, timedelta

#Criar duração de dias, horas, etc.
dia = timedelta(days=11)
horas = timedelta(hours=7,minutes=15,seconds=47)
hoje = date.today()


print(dia, hoje ,horas)




#Somar/subtrair datas com timedelta


amanha = hoje + dia
anteontem = hoje - timedelta(days=2)


print("Amanhã:", amanha)
print("Anteontem:", anteontem)




#Diferença entre dois datetime
inicio = datetime(2025,5,20,9,0)
fim    = datetime(2025,5,20,17,30)
duracao = fim - inicio
print(duracao)                # 8:30:00
print(duracao.total_seconds())# 30600.0 segundos