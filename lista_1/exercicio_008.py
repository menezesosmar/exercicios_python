# Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

ganho_hora = float(input('Quanto você ganha por hora? (Digite apenas números): '))
horas_trabalhadas = float(input('Agora, digite a quantidade de horas trabalhadas no mês: '))

salario = ganho_hora*horas_trabalhadas
print(f'O seu salário total é R${salario:.1f}.')