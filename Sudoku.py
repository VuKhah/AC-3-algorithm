class SudokuSolver:
    """
    Hàm khởi tạo:
        domains: Lưu trữ miền giá trị của từng biến trong trò chơi.
        arcs: Lưu trữ các ràng buộc
    """

    def __init__(self, grid):
        self.grid = grid
        self.size = len(grid)
        self.box_size = int(self.size**0.5)
        self.domains = {
            (r, c): list(range(1, self.size + 1)) if grid[r][c] == 0 else [grid[r][c]]
            for r in range(self.size)
            for c in range(self.size)
        }
        self.arcs = []
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i][j] == 0:
                    self.arcs.extend(self.get_arcs(i, j))
                    self.arcs.extend(self.get_arcs(j, i))

    # Hàm get_arcs: nhận giá trị vị trí của một biến và trả về danh sách các ràng buộc liên quan đến biến đó
    def get_arcs(self, row, col):
        arcs = []
        for i in range(self.size):
            if i != col:
                arcs.append(((row, col), (row, i)))
        for j in range(self.size):
            if j != row:
                arcs.append(((row, col), (j, col)))
        start_row, start_col = self.box_size * (row // self.box_size), self.box_size * (
            col // self.box_size
        )
        for i in range(start_row, start_row + self.box_size):
            for j in range(start_col, start_col + self.box_size):
                if (i, j) != (row, col):
                    arcs.append(((row, col), (i, j)))
        return arcs

    def solve(self):
        if self.AC_3():
            print("Sudoku giải được:")
            self.display_grid()
        else:
            print("Kỹ thuật AC_3 chưa giải được Sudoku này.")
            self.showDom()

    # Thuật toán AC_3
    def AC_3(self):
        while self.arcs:
            (xi, xj) = self.arcs.pop(0)
            if self.revise(xi, xj):
                if not self.domains[xi]:
                    return False
                for xk in self.get_arcs(*xi):
                    self.arcs.append((xk[1], xk[0]))
        return True

    def revise(self, xi, xj):
        revised = False
        for x in self.domains[xi]:
            if not any(x != y for y in self.domains[xj]):
                self.domains[xi].remove(x)
                revised = True
        return revised

    # Hiển thị lời giải sudoku
    def display_grid(self):
        for r in range(self.size):
            for c in range(self.size):
                if len(self.domains[(r, c)]) == 1:
                    print(f"{self.domains[(r, c)][0]} ", end="")
                else:
                    print("0 ", end="")
            print()

    def showDom(self):
        for i in range(self.size):
            for j in range(self.size):
                print(f"({i}, {j}) dom: {self.domains[(i, j)]}")


initial_board_0 = [
    [0, 3, 1, 6, 7, 0, 4, 0, 9],
    [0, 0, 0, 8, 3, 0, 0, 0, 0],
    [8, 2, 0, 0, 0, 0, 0, 1, 0],
    [0, 7, 4, 0, 0, 8, 1, 6, 0],
    [0, 8, 0, 0, 6, 0, 0, 0, 4],
    [9, 0, 2, 0, 0, 0, 0, 7, 3],
    [4, 9, 0, 0, 5, 7, 2, 3, 0],
    [2, 0, 0, 0, 9, 0, 5, 0, 7],
    [7, 0, 3, 2, 0, 0, 6, 0, 1],
]

initial_null_board = [
    [5, 0, 7, 6, 9, 0, 0, 0, 2],
    [9, 3, 0, 8, 0, 2, 7, 4, 5],
    [0, 0, 0, 3, 0, 7, 1, 0, 0],
    [0, 4, 5, 0, 6, 0, 3, 0, 8],
    [2, 0, 0, 4, 7, 0, 0, 0, 0],
    [0, 0, 0, 0, 8, 1, 0, 2, 0],
    [0, 0, 9, 0, 2, 5, 0, 1, 3],
    [3, 0, 0, 0, 0, 6, 0, 5, 7],
    [7, 0, 0, 1, 3, 0, 9, 8, 4],
]  #

solution = SudokuSolver(initial_board_0)
solution.solve()
