jogadas = ['pedra', 'papel', 'tesoura']

jogador = input('Faça sua jogada: ').lower()

# PC jogar sozinho
import random
posicao = random.randint(0, 2)
pc = jogadas[posicao]

if jogador not in jogadas:
    print('Jogada Invalida')
    
elif jogador == pc:
    print('Empate')
elif \
    (pc == 'pedra' and jogador == 'tesoura') or \
    (pc == 'tesoura' and jogador == 'papel') or \
    (pc == 'papel' and jogador == 'pedra'):
    print('PC ganhou')

else:
    print('Jogador Ganhou')