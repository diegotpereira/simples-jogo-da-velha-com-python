# https://github.com/matheus1760/jogo-da-velha

from view import apresentacao
from nomear_jogador import nomear_jogador

import time

def tabuleiro(elemento: list) -> None:
    
    """Método com uma lista de 'strings' como argumento para mostrar o tabuleiro"""
    
    print()
    
    print(f"{elemento[0]} | {elemento[1]} | {elemento[2]}")
    print(f"{elemento[3]} | {elemento[4]} | {elemento[5]}")
    print(f"{elemento[6]} | {elemento[7]} | {elemento[8]}")

print(apresentacao)

print('Pressione Enter para começar.')

input()

print("Carregando...")

time.sleep(1)


jogador1 = nomear_jogador("O", 1)
jogador2 = nomear_jogador("X", 2)

print("\nComo Jogar: ")

print("Cada casa do jogo da velha tem um número associado. Veja a ilustração:")

tabuleiro([numbers for numbers in range(1, 10)])


print("\nPara ganhar, é necessário 3 símbolos consecutivos.\n")

time.sleep(3)

print(f"{jogador1}(O)  vs {jogador2}(X)!")