# Crie uma função para Converter Celsius para Fahrenheit em uma Lista

def converter_temperatura(lista_celsius):
    return [(temp * 9/5) + 32 for temp in lista_celsius]

temperaturas_celsius = [0, 20, 30, 37, 100]
temperaturas_fahrenheit = converter_temperatura(temperaturas_celsius)

print(f"Temperaturas em Fahrenheit: {temperaturas_fahrenheit}")
