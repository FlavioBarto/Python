from datetime import date, datetime, timedelta
texto = "2025-05-20 14:30"
formato = "%Y-%m-%d %H:%M"
dt = datetime.strptime(texto, formato) #“string parse time”.
print(dt)
