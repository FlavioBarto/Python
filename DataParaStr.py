from datetime import date, datetime, timedelta
hoje = date.today()
# formata como "21/05/2025"
print(hoje.strftime("%d/%m/%Y"))




#para datetime completo
agora = datetime.now()
# ex.: "21-05-2025 14:45"
print(agora.strftime("%d-%m-%Y %H:%M"))