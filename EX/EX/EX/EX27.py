#Crie uma função que recebe uma data e retorna o dia da semana correspondente (segunda, terça...).

from datetime import datetime

def dia_da_semana(data_str):
    # Converte a string em um objeto datetime
    data = datetime.strptime(data_str, "%Y-%m-%d")
    
    # Lista com os nomes dos dias da semana em português
    dias = ['segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado', 'domingo']
    
    # Retorna o nome correspondente (0 = segunda, 6 = domingo)
    return dias[data.weekday()]
