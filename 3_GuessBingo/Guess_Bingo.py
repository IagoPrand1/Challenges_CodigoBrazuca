""" 
1. Gerar lista (cartela) com 5 valores aleatórios entre 1 e 75
2. Gerar uma valor aleatório entre 1 e 75 e verificar se ele está na lista
2.1. Contar o número de gerações
2.2. Caso esteja na lista, o valor é retirado
3. Termina com a lista vazia e o print do número de rodadas
 """

import random

def criar_cartela():

    cartela = []
    tamanhoCartela = 5

    while len(cartela) < tamanhoCartela:
        randomNum = random.randint(1,75)
        if not(randomNum in cartela):
            cartela.append(randomNum)
    
    return cartela

def sorteio():

    cartela = criar_cartela()

    print(f'Sua cartela {cartela}')
    listDrawNumber = []

    while len(cartela) != 0:
        drawNumber = random.randint(1,75)

        if not(drawNumber in listDrawNumber):
            listDrawNumber.append(drawNumber)
            print(f'Número sorteado: {drawNumber}')

            if drawNumber in cartela:
                cartela.remove(drawNumber)
                print(f'Parabéns, você acertou! Resta em sua cartela {cartela}')

    return len(listDrawNumber)

print('Você completou sua cartela em ', sorteio())
                


