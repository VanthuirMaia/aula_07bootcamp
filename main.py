from etl import ler_csv, filtrar_entregas, somar_valor_dos_produtos

path_arquivo = "vendas.csv"

lista_de_produtos = ler_csv(path_arquivo)
produtos_entregues = filtrar_entregas(lista_de_produtos)
valor_dos_produtos_entregues = somar_valor_dos_produtos(produtos_entregues)
print(valor_dos_produtos_entregues)