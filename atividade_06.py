# Crie uma função para Encontrar Valores Ausentes em uma Sequência

def encontrar_valores_ausentes(lista: int) -> int:
    if not lista:
        return []

    minimo, maximo = min(lista), max(lista)
    conjunto_completo = set(range(minimo, maximo + 1))
    valores_ausentes = conjunto_completo - set(lista)

    return sorted(valores_ausentes)

valores = [1, 2, 4, 6, 7, 10]
ausentes = encontrar_valores_ausentes(valores)

print(f"Valores ausentes: {ausentes}")
