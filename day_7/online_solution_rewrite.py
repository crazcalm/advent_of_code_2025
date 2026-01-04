import fileinput
from pprint import pprint


def get_traverse(rows, cols, grid):
    # made this into a closure to prevent global variables
    memo = {}
    

    def traverse(row, col):
        if row < 0 or row >= rows or col < 0 or col > cols:
            return 1

        if (row, col) in memo:
            return memo[(row, col)]
    
        current_cell = grid[row][col]

        if current_cell == "^":
            left_path = traverse(row + 1, col - 1)
            right_path = traverse(row + 1, col + 1)
            result = left_path + right_path

        else:
            # current_cell == "." case
            result = traverse(row + 1, col)


        memo[(row, col)] = result
        return result
    return traverse

def main():
    grid = list(fileinput.input())
    rows = len(grid) - 1
    cols = len(grid[0]) - 1
    beam = grid[0].find("S")
    
    traverse = get_traverse(rows, cols, grid)
    total_paths = traverse(1, beam)
    print(total_paths)


if __name__ == "__main__":
    main()

