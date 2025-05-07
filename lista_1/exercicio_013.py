# Tendo como dado de entrada a altura (h) de uma pessoa,
# construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#   Para homens: (72.7h) - 58
#   Para mulheres: (62.1h) - 44.7

sexo = input('Qual seu sexo? (M/F):')
altura = float(input('Qual é sua altura? :'))
peso_ideal = float()
if sexo in 'mM' :
    peso_ideal = ((72.7*altura) - 58)
    print(f'Seu peso ideal é {peso_ideal}')
elif sexo in'fF':
    peso_ideal = ((62.1 * altura) - 44.7)
    print(f'Seu peso ideal é {peso_ideal}')
else:
    print('Sexo incorreto. Tente novamente.')




