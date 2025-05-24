def checkforvalid(grid, row, col, number):
    #CHECK FOR HORIZONTAL
    for i in range(9):
        if grid[i][col] == number:
            return False
    #CHECK FOR VERTICAL
    for i in range(9):
        if grid[row][i] == number:
            return False
    #CHECK IN BLOCK
    row_conner = row - row % 3
    col_conner = col - col % 3
    for x in range(3):
        for y in range(3):
            if grid[x + row_conner][y + col_conner] == number:
                return False
    #YOU CAN PUT THE NUMBER IN THE GRID
    return True

def solve(grid, row, col):

    #CHECK IF IT IS FINISH OR NOT
    if col == 9:
        if row == 8:
            return True
        #IF IT AT THE END OF THE ROW(COL = 9) THEN INCREASE THE ROW AND RESET THE COL
        row += 1
        col = 0
    #CHECK IF CURRENT CELL IS HAVE VALUE OR NOT
    if grid[row][col] > 0:
        return solve(grid, row, col + 1)

    for i in range(1,10):

        if checkforvalid(grid, row, col, i):
            grid[row][col] = i

            if solve(grid, row, col + 1):
                return True

        grid[row][col] = 0

    return False

grid = [
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

if solve(grid, 0, 0):
    for i in range(9):
        for j in range(9):
            print(grid[i][j], end = ' ')
        print()
else:
    print("THIS SUDOKU CAN NOT BE SOLVE")