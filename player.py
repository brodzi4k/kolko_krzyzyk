import random
import string
import math

row_y = list(string.ascii_uppercase)

class Player():
    # Wbudowany dekorator, definiuje metode statyczna w klasie w Py
    @staticmethod
    def parse_cords(raw):
        try:
            if raw[0].isalpha():
                return (int(raw[1:])-1, row_y.index(raw[0]))
            elif raw[-1].isalpha():
                return (int(raw[:-1])-1, row_y.index(raw[-1]))
            else:
                return None
        except Exception:
            return None
    
    def get_move(self, state):
        cords = self.parse_cords(input("Teraz twoja kolej, wprowadź ruch w formcie XY \n Gdzie X - wiersz, Y - kolumna").upper())
        while cords not in state.possible_moves():
            cords = self.parse_cords(input("Sprobuj ponownie, nie ma takiego pola lub jest zajete D: ").upper())
        return cords

class RandomPlayer():
    def get_move(self, state):
        return random.choice(state.possible_moves())
        

class Bot():
    def __init__(self, player, search_depth):
        self.player = player
        self.other_player = 'O' if player == 'X' else 'X'
        self.search_depth = search_depth
    
    def get_move(self, state):
        return self.minimax(state, 0, -math.inf, math.inf, True)['move']

    def minimax(self, state, depth, alpha, beta, maximizing):
        if state.gameover() or depth == self.search_depth:
            # zwraca optymalny ruch
            return {'move': None, 'score': state.evaluate(self.player)}

        if maximizing:
            best = {'move': None, 'score': -math.inf}
            for move in state.possible_moves():
                state.set_move(move, self.player)
                check = self.minimax(state, depth+1, alpha, beta, False)
                state.set_move(move, ' ')
                check['move'] = move

                if check['score'] > best['score']:
                    best = check
                
                alpha = max(alpha, best['score'])
                if best['score'] >= beta:
                    break
            return best
        else:
            best = {'move': None, 'score': math.inf}
            for move in state.possible_moves():
                state.set_move(move, self.other_player)
                check = self.minimax(state, depth+1, alpha, beta, True)

                # cofnij
                state.set_move(move, ' ')
                check['move'] = move

                if check['score'] < best['score']:
                    best = check
                
                beta = min(beta, best['score'])
                if best['score'] <= alpha:
                    break
            return best