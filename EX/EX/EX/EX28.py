#Gere uma lista com as datas dos próximos 15 dias a partir de hoje.

from datetime import datetime, timedelta

hoje = datetime.today()
proximos_15_dias = []

for i in range(1, 16):
    dia = hoje + timedelta(days=i)
    proximos_15_dias.append(dia.strftime("%Y-%m-%d"))

# Exibe a lista
for data in proximos_15_dias:
    print(data)