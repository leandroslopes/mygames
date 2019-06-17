print('\n******************************')
print('*     Jogo da Adivinhacao    *')
print('******************************')

numero_secreto = 33
pontos = 1000

nivel = int(input('\nEscolha o nivel do jogo [1, 2, 3]: '))
while(nivel not in [1, 2, 3]):
    print('\nNivel nao existente!')
    nivel = int(input('Escolha o nivel do jogo [1, 2, 3]: '))

if nivel == 1:
    total_de_tentativas = 20
elif nivel == 2:
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

for rodada in range(1, total_de_tentativas + 1):
    print('\nTentativa {} de {}'.format(rodada, total_de_tentativas))
    
    chute = int(input('\nFaca seu chute: '))
    print('Voce digitou {}'.format(chute))

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print('\nVoce acertou!')
        break
    elif maior:
        print('\nVoce errou! Chute maior que numero secreto')
        pontos = pontos - abs(numero_secreto - chute)
        print('Pontuacao parcial: {}'.format(pontos))
    elif menor:
        print('\nVoce errou! Chute menor que numero secreto')
        pontos = pontos - abs(numero_secreto - chute)
        print('Pontuacao parcial: {}'.format(pontos))

print('\nPontuacao final: {}'.format(pontos))
print('Fim de Jogo')