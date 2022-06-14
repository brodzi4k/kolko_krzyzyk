import string
from copy import deepcopy

row_y = list(string.ascii_uppercase)

class Board():
    def __init__(self, width, height, winstreak):
        self.width = width
        self.height = height
        self.winstreak = winstreak
        # Teraz musimy utworzyc tablicę pustych komorek o zadanych wymiarach
        self.board = [ [' ' for x in range(width)] for y in range(height) ]

    # Czyszczenie tablicy
    def reset(self):
        self.board = [ [' ' for x in range(self.width)] for y in range(self.height) ]

    # Ruch na planszy
    def set_move(self, pos, player):
        self.board[pos[1]][pos[0]] = player

    # Zwracanie listy pustych komorek
    def possible_moves(self):
        moves = []
        for y, row in enumerate(self.board):
            for x, cell in enumerate(row):
                if cell == ' ':
                    moves.append((x, y))

        return moves

    # Przypadek gdy plansza jest pelna lub przegralismy
    def gameover(self):
        return len(self.possible_moves()) == 0 or self.iswin('X') or self.iswin('O')

    # Sprawdzenie wygranej
    def iswin(self, player):
        # Sprawdzenie przekatnych
        for y in range(self.height-self.winstreak+1):
            for x in range(self.width-self.winstreak+1):
                if all([self.board[y+i][x+i] == player for i in range(self.winstreak)]):
                    return True
        
        for y in range(self.winstreak-1,self.height):
            for x in range(self.width-self.winstreak+1):
                if all([self.board[y-i][x+i] == player for i in range(self.winstreak)]):
                    return True

        # Sprawdzenie wierszy
        for y in range(self.height):
            for x in range(self.width-self.winstreak+1):
                if all([self.board[y][x+i] == player for i in range(self.winstreak)]):
                    return True

        # Sprawdzenie kolumn
        for y in range(self.height-self.winstreak+1):
            for x in range(self.width):
                if all([self.board[y-i][x] == player for i in range(self.winstreak)]):
                    return True

        return False
    
    def evaluate(self, player):
        other_player = 'O' if player == 'X' else 'X'
        if self.iswin(player):
            return (len(self.possible_moves()) + 1)
        elif self.iswin(other_player):
            return -(len(self.possible_moves()) + 1)
        else:
            return 0
    
    def render(self):

        print(f"  {'   '.join([str(i+1) for i in range(self.width)])}")

        for index, row in enumerate(self.board):
            print(f"{row_y[index]} {' | '.join(row)}")
            if index + 1 < self.height:
                print("  " + '-'*(self.width*4-3))