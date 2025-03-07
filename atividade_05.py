# Crie uma função para Calcular Desvio Padrão de uma Lista

import math

def calcular_desvio_padrao(lista: list[float]) -> float:
    if len(lista) < 2:
        return 0  # O desvio padrão não faz sentido para listas com menos de 2 valores

    media = sum(lista) / len(lista)
    variancia = sum((x - media) ** 2 for x in lista) / len(lista)  # Para amostras use (len(lista) - 1)
    return math.sqrt(variancia)

valores = [10, 20, 30, 40, 50]
desvio_padrao = calcular_desvio_padrao(valores)

print(f"Desvio padrão: {desvio_padrao:.2f}")
