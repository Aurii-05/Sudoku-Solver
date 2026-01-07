import random

class Grid:
    def __init__(self, key=None):
        self.__freshgrid()
        if key:
            self.key = key

            for i in range(9):
                for j in range(9):
                    self.grid[i][j] = int(self.key[0])
                    self.key = self.key[1:]
        else:
            self.key = None

    def __freshgrid(self):
        self.grid = [[0 for _ in range(9)] for _ in range(9)]
        return self.grid
    
    def conv_grid_to_key(self):
        if self.grid:
            _key = ''
            for i in range(9):
                for j in range(9):
                    _key += str(self.grid[i][j])
            return _key
        else:
            return ''

    def detect_spaces(self):
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == 0:
                    return (i,j)
        return False
    
    def check_valid_input(self, num, postion):
        if not self.grid[postion[0]][postion[1]] == 0:
            return False
        for col in self.grid[postion[0]]:
            if col == num:
                return False
        for row in range(9):
            if self.grid[row][postion[1]] == num:
                return False
        box_x = postion[1] // 3
        box_y = postion[0] // 3
        for i in range(box_y*3, box_y*3 + 3):
            for j in range(box_x * 3, box_x*3 + 3):
                if self.grid[i][j] == num:
                    return False
        return True
    

    def solve(self):
        find = self.detect_spaces()
        if not find:
            return True
        else:
            row, col = find
        for i in range(1,10):
            if self.check_valid_input(i, (row, col)):
                self.grid[row][col] = i

                if self.solve():
                    return True

                self.grid[row][col] = 0
        return False

    def print_grid(self):
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - - - ")

            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")

                if j == 8:
                    print(self.grid[i][j])
                else:
                    print(str(self.grid[i][j]) + " ", end="")

def solve_sudoku(grid_key):
    grid_obj = Grid(grid_key)
    grid_obj.solve()
    return grid_obj.conv_grid_to_key()

if __name__ == '__main__':
    
    grid_str = input("Enter the Sudoku grid row by row, with no seperating spaces, as in Row 1 Col 1-9 then Row 2 Col 1-9, a blank space should be 0:\n")
    solved_grid_key = solve_sudoku(grid_str)
    
    print("Original Sudoku:")
    original_grid = Grid(grid_str)
    original_grid.print_grid()
    print("\nSolved Sudoku:")
    solved_grid = Grid(solved_grid_key)
    solved_grid.print_grid()
