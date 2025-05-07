# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.
# Fórmula: F = (C * 1,8) + 32.

celsius = float(input('Insira a temperatura (ºC): '))
farenheit = (celsius*1.8) + 32
farenheit_arredondado = round(farenheit)

print(f'{celsius}ºC em Farenheit: {farenheit_arredondado:.1f}ºC.')

