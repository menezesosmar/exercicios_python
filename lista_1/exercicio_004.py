# Faça um programa que peça as 4 notas bimestrais e mostre a média.
notas_bimestrais = float()
soma = float()
media = float()
for i in range(1,5):
    notas_bimestrais = float(input(f'Digite a {i}ª nota: '))
    soma += notas_bimestrais
media = soma/4

print(f'Sua média de notas é: {media:.1f}')
