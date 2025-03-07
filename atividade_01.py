# Crie uma função para calcular Média de Valores em uma Lista

def caucular_media(list: list[float]) -> float:
    return sum(list) / len(list)

lista = [1, 2, 5, 6, 8, 9, 4, 8, 5, 9]

resultado = caucular_media(lista)

print(resultado)
