import random
import time
import os

# mostrar titulo


def titulo():
    print('\n---------------------------------------------------------')
    print('\t Advinhe o número')
    print('\n---------------------------------------------------------')


# gerador de número aleatório
def gerar_numero_aleatorio():
    numero_gerado = random.randrange(1, 20+1)
    return numero_gerado

# lógica


def gerador(numero, tentativa):
    while True:
        try:
            chute = int(
                input('\nChute o numero que foi gerado entre 1 e 20. \nResposta: '))
            if chute > 20 or chute < 1:
                time.sleep(1)
                print('\nApena um número entre 1 e 20... tente de novo!')
                time.sleep(1)
            elif chute > numero:
                time.sleep(1)
                print(
                    f'\nO número que gerei foi menor que {chute}, tente novamente!')
                tentativa += 1
            elif chute < numero:
                print(
                    f'O número que gerei foi maior que {chute} tente novamente!')
                time.sleep(1)
                tentativa += 1
            elif chute == numero:
                time.sleep(1)
                print(
                    f'\nVocê acertou! parabens! seu número de tentativas foi {tentativa}...\n')
                time.sleep(1)
                escolha = input('Deseja jogar novamente? (s/n): ')
                if escolha.lower == 's':
                    print('Começando novamente...')
                    time.sleep(3)
                    numero = gerar_numero_aleatorio()
                    tentativa = 0
                    os.system('cls')
                    titulo()
                    continue
                elif escolha.lower == 'n':
                    print('\nObrigado por jogar!')
                    break
        except ValueError:
            print('\nDigite um numero inteiro!')
            time.sleep(1)


titulo()
input('Digite ENTER para iniciar...')
numero = gerar_numero_aleatorio()
tentativas = 0
gerador(numero, tentativas)
