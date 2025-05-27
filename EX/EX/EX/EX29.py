#Dada uma data de venda e a data atual, informe se a venda está dentro da garantia de 90 dias.

from datetime import datetime

def dentro_da_garantia(data_venda_str):
    # Converte a string da data de venda para datetime
    data_venda = datetime.strptime(data_venda_str, "%Y-%m-%d")
    
    # Pega a data atual
    hoje = datetime.today()
    
    # Calcula a diferença em dias
    dias_passados = (hoje - data_venda).days
    
    # Verifica se está dentro da garantia de 90 dias
    if dias_passados <= 90:
        return True
    else:
        return False
