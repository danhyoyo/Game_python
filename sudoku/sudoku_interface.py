import tkinter as tk

# Các hàm bạn đã viết
def checkforvalid(grid, row, col, number):
    for i in range(9):
        if grid[i][col] == number:
            return False
    for i in range(9):
        if grid[row][i] == number:
            return False
    row_conner = row - row % 3
    col_conner = col - col % 3
    for x in range(3):
        for y in range(3):
            if grid[x + row_conner][y + col_conner] == number:
                return False
    return True

def solve(grid, row, col):
    if col == 9:
        if row == 8:
            return True
        row += 1
        col = 0
    if grid[row][col] > 0:
        return solve(grid, row, col + 1)
    for i in range(1, 10):
        if checkforvalid(grid, row, col, i):
            grid[row][col] = i
            if solve(grid, row, col + 1):
                return True
        grid[row][col] = 0
    return False

# Grid đề bài ban đầu
initial_grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# if solve(initial_grid, 0, 0):
#     for i in range(9):
#         for j in range(9):
#             print(initial_grid[i][j], end = '')
#         print()
# else:
#     print("THIS SUDOKU CAN NOT BE SOLVE")
class SudokuGUI:
    def __init__(self, root, grid):
        self.root = root
        self.root.title("Sudoku Solver")
        self.entries = []
        self.grid_data = [row[:] for row in grid]  # sao chép để không sửa original grid

        for i in range(9):
            row = []
            for j in range(9):
                e = tk.Entry(root, width=3, font=('Arial', 18), justify='center')
                e.grid(row=i, column=j, padx=2, pady=2)
                if grid[i][j] != 0:
                    e.insert(0, str(grid[i][j]))
                    e.config(state="disabled", disabledforeground="black")
                row.append(e)
            self.entries.append(row)

        solve_button = tk.Button(root, text="Solve", command=self.solve_sudoku)
        solve_button.grid(row=9, column=0, columnspan=9, pady=10)

    def read_grid(self):
        grid = []
        for i in range(9):
            row = []
            for j in range(9):
                val = self.entries[i][j].get()
                row.append(int(val) if val.isdigit() else 0)
            grid.append(row)
        return grid

    def fill_grid(self, grid):
        for i in range(9):
            for j in range(9):
                if self.entries[i][j]['state'] == 'normal':
                    self.entries[i][j].delete(0, tk.END)
                    self.entries[i][j].insert(0, str(grid[i][j]))

    def solve_sudoku(self):
        grid = self.read_grid()
        if solve(grid, 0, 0):
            self.fill_grid(grid)
        else:
            print("Không thể giải được Sudoku này.")

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuGUI(root, initial_grid)
    root.mainloop()
