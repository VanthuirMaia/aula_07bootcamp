# Crie uma função para Filtrar Dados Acima de um Limite

def filtrar_limite(lista: list[float], limite: float) -> list[float]:
    return [valor for valor in lista if valor >= limite]

valores = [10, 20, 30, 40, 50]
limite = 15

resultado = filtrar_limite(valores, limite)
print(f"Valores acima do {limite} são {resultado}")