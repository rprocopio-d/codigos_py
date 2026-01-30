# variveis: potencia, largura, comprimento,
# numeroLampadas

# a cada m² precisa de 3 watts // 
# a cada 3m² tem um bocal

import math

potencia = int(input('Digite a potencia da lampada em watts: '))
largura = float(input('Digite a largura do comodo (em metros): '))
comprimento = float(input('Digite o comprimento do comodo (em metros): '))

# etapa dos calculos
# saber quantos m² eu tenho
area = largura * comprimento

# saber quantos watts necessito
potencia_necessaria = area * 3

# saber quantas lampadas eu preciso para 
# chegar a potencia_necessaria
numero_lampadas = \
math.ceil(potencia_necessaria/potencia)

# calcular o numero de bocais disponiveis
numero_bocais = int(area/3)

print(10*'-')
print(f'Area do Comodo: {area:.2f}m²')
print(f'Potencia necessaria: {potencia_necessaria}')
print(f'Numero de Lampadas: {numero_lampadas}')
print(f'Numero de Bocais Estimados: {numero_bocais}')

if numero_lampadas > numero_bocais:
    print('Numero de Bocais Insuficiente')