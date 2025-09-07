class Player:
    def __init__(self, symbol):
        self.symbol = symbol

class Board:
    def __init__(self):
        self.grid = [[' ' for _ in range(3)] for _ in range(3)]

    def display(self):
        print("-------------")
        for i in range(3):
            print("| ", end="")
            for j in range(3):
                print(self.grid[i][j], "| ", end="")
            print("\n-------------")

    def place_symbol(self, row, col, symbol):
        if self.grid[row][col] == ' ':
            self.grid[row][col] = symbol
            return True
        return False

    def check_win(self, symbol):
        for i in range(3):
            if self.grid[i][0] == symbol and self.grid[i][1] == symbol and self.grid[i][2] == symbol:
                return True
            if self.grid[0][i] == symbol and self.grid[1][i] == symbol and self.grid[2][i] == symbol:
                return True
        if self.grid[0][0] == symbol and self.grid[1][1] == symbol and self.grid[2][2] == symbol:
            return True
        if self.grid[0][2] == symbol and self.grid[1][1] == symbol and self.grid[2][0] == symbol:
            return True
        return False

    def is_full(self):
        for i in range(3):
            for j in range(3):
                if self.grid[i][j] == ' ':
                    return False
        return True

class Game:
    def __init__(self):
        self.player1 = Player('X')
        self.player2 = Player('O')
        self.board = Board()
        self.player1_turn = True

    def play(self):
        while True:
            self.board.display()
            current = self.player1 if self.player1_turn else self.player2
            row, col = map(int, input(f"Player {current.symbol}, enter row and column (1-3): ").split())
            row -= 1
            col -= 1
            if 0 <= row < 3 and 0 <= col < 3:
                if self.board.place_symbol(row, col, current.symbol):
                    if self.board.check_win(current.symbol):
                        self.board.display()
                        print(f"Player {current.symbol} wins!")
                        break
                    if self.board.is_full():
                        self.board.display()
                        print("It's a draw!")
                        break
                    self.player1_turn = not self.player1_turn
                else:
                    print("That spot is taken. Try again.")
            else:
                print("Invalid input. Try again.")

if __name__ == "__main__":
    Game().play()
