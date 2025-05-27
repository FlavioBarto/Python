#Dado um horário de início e fim do expediente (ex: 09:00 às 17:30), calcule a duração do expediente em horas.

from datetime import datetime

inicio_str = '09:00'
fim_str = '17:30'

# Converte strings para objetos datetime (apenas hora)
inicio = datetime.strptime(inicio_str, "%H:%M")
fim = datetime.strptime(fim_str, "%H:%M")

# Calcula a diferença
duracao = fim - inicio

# Converte para horas
horas = duracao.total_seconds() / 3600

print(f'Duração do expediente: {horas:.2f} horas')
