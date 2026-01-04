"""
Here is the reference code I used -- https://gist.github.com/sayujya-apte/bf3f0e56fc26bc51ebc79cfeb5ce0c04
"""

import fileinput

memo = {}

def traverse(row, col, rows, cols, grid):
    if row < 0 or row >= rows or col < 0 or col > cols:
        return 1

    if (row, col) in memo:
        return memo[(row, col)]
    
    current_cell = grid[row][col]

    if current_cell == "^":
        left_path = traverse(row + 1, col - 1, rows, cols, grid)
        right_path = traverse(row + 1, col + 1, rows, cols, grid)
        result = left_path + right_path

    elif current_cell == ".":
        result = traverse(row + 1, col, rows, cols, grid)

    else:
        return 0

    memo[(row, col)] = result
    return result

def main():
    grid = list(fileinput.input())
    rows = len(grid) - 1
    cols = len(grid[0]) - 1
    beam = grid[0].find("S")

    total_paths = traverse(1, beam, rows, cols, grid)
    print(total_paths)


if __name__ == "__main__":
    main()

    
