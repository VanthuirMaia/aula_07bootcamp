# Crie uma função para Contar Valores Únicos em uma Lista

def contar_valores(lista: list[int]) -> int:
    return len(set(lista))

valores = [10, 20, 30, 10, 20, 40, 50, 30]
quantidade_unicos = contar_valores(valores)

print(f"Quantidade de valores únicos: {quantidade_unicos}")
