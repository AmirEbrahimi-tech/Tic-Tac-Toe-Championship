import random
from piece import Piece, Type

class Grid:
    def __init__(self):
        self.grid = [[Piece() for _ in range(3)] for _ in range(3)]

    def display(self):
        for i in range(3):
            print("-------------")
            for j in range(3):
                piece = self.get_piece(i, j)
                t = piece.get_type()
                age = piece.get_age()
                if t == Type.NONE:
                    print(f"| {i * 3 + j + 1} ", end="")
                elif t == Type.O:
                    print(f"| \033[1;35mO\033[0m " if age == 1 else "| \033[1;31mO\033[0m ", end="")
                elif t == Type.X:
                    print(f"| \033[1;36mX\033[0m " if age == 1 else "| \033[1;34mX\033[0m ", end="")
            print("|")
        print("-------------")

    def set_piece(self, row, col, t):
        piece = self.get_piece(row, col)
        piece.set_type(t)
        piece.set_age(7)

    def get_piece(self, row, col):
        return self.grid[row][col]

    def num_piece(self, t):
        return sum(1 for row in self.grid for p in row if p.get_type() == t)

    def set_all_pieces(self):
        for row in self.grid:
            for p in row:
                if p.get_age() > 0:
                    p.lose_age()

    def input(self, t, turn):
        print(f"\033[4;31mRed\033[0m" if turn % 2 == 0 else "\033[4;34mBlue\033[0m", "it's your turn.\n\033[1;31mGO!\033[0m")
        while True:
            try:
                pos = int(input("Where do you want to place it? "))
                if not (1 <= pos <= 9):
                    raise ValueError
                row, col = (pos - 1) // 3, (pos - 1) % 3
                if self.get_piece(row, col).get_type() != Type.NONE:
                    print("Oops! Choose a \033[1;33mnon-occupied\033[0m place!")
                    continue
                break
            except ValueError:
                print("Choose one between 1 - 9.")
        self.set_piece(row, col, t)

    def game_finished(self):
        winner = None
        g = self.grid
        # Diagonals
        if g[0][0] == g[1][1] == g[2][2]:
            winner = g[1][1].get_type()
        elif g[2][0] == g[1][1] == g[0][2]:
            winner = g[1][1].get_type()
        else:
            for i in range(3):
                if g[i][0] == g[i][1] == g[i][2]:
                    winner = g[i][1].get_type()
                    break
                if g[0][i] == g[1][i] == g[2][i]:
                    winner = g[1][i].get_type()
                    break
        return winner

    def set_one_random_piece(self, t):
        if self.num_piece(Type.NONE) == 0:
            return
        while True:
            pos = random.randint(0, 8)
            row, col = pos // 3, pos % 3
            if self.get_piece(row, col).get_type() == Type.NONE:
                self.set_piece(row, col, t)
                break

    def get_status(self):
        for i in range(3):
            for j in range(3):
                p = self.get_piece(i, j)
                print(f"cell {i} - {j} : {p.get_type().name} age : {p.get_age()}")
