from datetime import date, datetime, timedelta
#Criando uma data atual
hoje = date.today()
print(hoje)


#Criando uma data específica
aniversario = date(1999, 3, 15)
print(aniversario)


#Criando um timestamp (data + hora)
agora = datetime.now()
print(agora)


#Criando um datetime específico
dt_evento = datetime(2025, 5, 20, 14, 30, 0)
print(dt_evento)
