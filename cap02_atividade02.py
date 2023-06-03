from os import system
from random import randint
      

system('cls') # limpa a tela

print('***************************************')
print('****** Adivinhe qual é o número  ******')
print('***************************************')


# Relembrar constantes e variávies
numero_secreto = 83 #constante

rodada = 0
total_de_tentativas = 3
ponto = 1000
acerto = False

print('Qual o nível de dificuldade?')
print('(1 padawan \n(2) cavaleiro \n(3) mestre Jedi)')
nivel = int(input('\nDefina o nível'))

    
    # é Preciso converte a string para int, de modo a haver comparação correta no if
if nivel == 1:
        total_de_tentativas = 20
elif nivel == 2:
        total_de_tentativas = 10
else:
        total_de_tentativas = 5

        
try:
    tentativa_int = int(tentativa)
except ValueError:
        print('Valor inválido. Informe um número inteiro')
        break
except Exception as e:
        print(f'ERRO: {e}')
        break
else:
        pass
        # print('\nentrou no ELSE')
    finally:
        pass
        # print('\nentrou no FINALLY')

    # segundo o guia de estilo para Python, é sempre, que possível, necessário melhorar 
    # a legibilidade do código.
    # Mudaremos i IF para uma  estrutura melhor

    acerto = tentativa_int == numero_secreto
    ehmaior = tentativa_int > numero_secreto
    ehmenor = tentativa_int < numero_secreto

    # Nova estrututa de IFs
    if acerto:
        print(f'Boa tentativa. ACERTOU!!!! \nFez {pontos}')
        #exit()
        break
    else:
        pontos_proximidade = 50 - abs(numero_secreto - tentativa_int)
        pontos = pontos - pontos_a_perder + pontos_proximidade

        print('Não foi dessa vez. ERROU!!!!')
        if ehmaior:
            print('Sua tentativa foi MAIOR que o número secreto.')
        if ehmenor:
            print('Sua tentativa foi MENOR que o número secreto.')
        if (rodada < total_de_tentativas)
            print(f'Sua pontuação atual: {pontos}')
        else:
            print('\n-------------------')
            print(f'O número secreto era {numero_secreto}')
            print(f'Sua pontuaçaõ final {pontos}')
            print('------------------------------')
        
if not acerto:
    print('GAME OVER!')
print('Obrigado por participar')