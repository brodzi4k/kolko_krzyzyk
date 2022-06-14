from board import Board
import player
from os import system
#import time

def main():
    print("Witaj w grze kolko i krzyzyk")
    print("Aby wygrac, zdobadz cala przekatna, wiersz lub kolumne")
    print("Plansza bedzie kwadratowa, jaki chcesz rozmiar? ")
    size = int(input())
    print("Ilosc znakow potrzebnych, by wygrac? ")
    number = int(input())
    print("Głębokość algorytmu? ")
    level = int(input())
    board = Board(size, size, number)

    playerX = player.Player()
    playerO = player.Bot('O', level)

    while not board.gameover():
        board.render()
        moveX = playerX.get_move(board)
        board.set_move(moveX, 'X')

        if board.gameover(): break
        board.render()
        moveO = playerO.get_move(board)
        board.set_move(moveO, 'O')
        print(f"Ruch komputera: {moveO}")
    board.render()


    if board.iswin('X'):
        print('Wygrales!')
    elif board.iswin('O'):
        print('Przegrales!')
    elif len(board.possible_moves()) == 0:
        print('Remis!')

main()

#%%
