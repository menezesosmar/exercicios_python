# Faça um Programa que peça 2 números inteiros e um número real.
# Calcule e mostre:
# a) O produto do dobro do primeiro com metade do segundo.
# b) A soma do triplo do primeiro com o terceiro.
# c) O terceiro elevado ao cubo.

num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite o segundo número inteiro: '))
num3 = float(input('Agora, digite o um número qualquer: '))

calc1 = ((num1*2) * (num2/2))
calc2 = ((num1*3)+ num3)
calc3 = num3**3

print(f'Aqui estão os seus cálculos:\n'
      f'O produto do dobro do primeiro com a metade do segundo: {calc1}\n'
      f'A soma do triplo do primeiro com o terceiro: {calc2}\n'
      f'O terceiro elevao ao cubo: {calc3}')




