class NQueens:
    def __init__(self, size):
        self.size = size
        self.solutions = []
        self.board = []

    def is_valid(self, row, col):
        for i in range(row):
            if self.board[i] == col or abs(self.board[i] - col) == abs(i - row):
                return False
        return True

    def solve(self, row=0):
        if row == self.size:
            self.solutions.append(self.board[:])
            return
        for col in range(self.size):
            if self.is_valid(row, col):
                self.board.append(col)
                self.solve(row + 1)
                self.board.pop()

    def print_solutions(self):
        for solution in self.solutions:
            print(f"Found solution: {solution}")
            for col in solution:
                row = ['0'] * self.size
                row[col] = '1'
                print("[" + ''.join(row) + "]")
            print()


if __name__ == "__main__":
    n = int(input("Enter the value of n: "))
    solver = NQueens(n)
    solver.solve()
    solver.print_solutions()