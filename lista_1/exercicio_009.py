# Faça um programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em Graus Celsius
# Fórmula: C = (5* (f-32) /9

farenheit = float(input('Insira a temperatura (ºF): '))
celsius = 5* (farenheit-32)/9
celsius_arredondado = round(celsius)
print(f'º{farenheit}F em graus Celsius: º{celsius_arredondado:.1f}C')