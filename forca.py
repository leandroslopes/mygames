import random

def imprime_mensagem_abertura():
    print('\n*********************************')
    print('***Bem vindo ao jogo da Forca!***')
    print('*********************************\n')

def carrega_palavra_secreta(): 
    arquivo = open('palavras.txt', 	'r')
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
	   
    arquivo.close()
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    
    return palavra_secreta
    
def inicializa_letras_acertadas(palavra):
    return	['_' for letra in palavra]
    
def pede_chute():
    chute = input('\nQual letra? ')
    chute = chute.strip().upper()
    return chute
    
def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    posicao = 0
    for letra in palavra_secreta:
        if	(chute == letra):
            letras_acertadas[posicao] = letra
        posicao += 1

def imprime_mensagem_vencedor():
    print('\nVoce ganhou!')

def imprime_mensagem_perdedor(palavra_secreta):
    print('Puxa, voce foi enforcado!')	
    print('A palavra era {}'.format(palavra_secreta))
    print("     _______________     ")
    print("    /               \    ")
    print("   /                 \   ")
    print(" //                   \/\\")
    print(" \|   XXXX    XXXX     |/")
    print("  |   XXXX    XXXX     |/")
    print("  |   XXX      XXX     | ")
    print("  |                    | ")
    print("  \__     XXX        __/ ")
    print("    |\    XXX       /|	  ")
    print("    | |            | |   ")
    print("    | I I I I I I I  |	  ")
    print("    | I I I I I I    |	  ")
    print("    \_              _/   ")
    print("      \_          _/     ")
    print("        \________/       ")

def jogar():
    imprime_mensagem_abertura()
    
    palavra_secreta = carrega_palavra_secreta()
    
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)
    
    acertou 	=	 False
    enforcou = False
    erros = 0

    while(not	acertou 	and	not	enforcou):
        chute = pede_chute()

        if (chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
        
        enforcou = erros == 6
        acertou = '_' not in letras_acertadas
        
        print(letras_acertadas)

    if acertou:
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)