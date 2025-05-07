# Faça um programa que peça dois números e imprima a soma.
num = int()
soma = int()
for i in range(1,3):
    num = int(input(f'Digite o {i} número: '))
    soma += num
print(f'A soma dos dois números é {soma}')