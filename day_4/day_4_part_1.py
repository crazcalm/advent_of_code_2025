import fileinput
from pprint import pprint

class Grid:
    def __init__(self, grid, rolls="@", mark="x"):
        self.grid = grid
        self.x_bounds = len(grid[0])
        self.y_bounds = len(grid)
        self.rolls = rolls
        self.mark = mark

        self.x = 0
        self.y = 0

    def _increment(self):
        self.x += 1

        if self.x >= self.x_bounds:
            self.y += 1

            if self.x >= self.x_bounds and self.y >= self.y_bounds:
                raise StopIteration

            self.x = 0
        return self.x, self.y
            
    def __iter__(self):
        return self

    def __next__(self):
        value = None
        while value != self.rolls:
            x,y = self._increment()
            value = self.grid[y][x]
            if value == self.rolls:
                return (value, x, y)

    def neighbors_count(self, x, y):
        neighbors = []
        possible_homes = [
            (x - 1, y -1),
            (x - 1, y),
            (x - 1, y + 1),
            (x, y + 1),
            (x + 1, y + 1),
            (x + 1, y),
            (x + 1, y - 1),
            (x , y - 1),
        ]

        homes = [(x, y) for x, y in possible_homes if x >=0 and x <self.x_bounds and y >= 0 and y < self.y_bounds]
        
        for x, y in homes:
            neighbors.append(self.grid[y][x])

        return sum([1 if person == self.rolls else 0 for person in neighbors])
            
def main():
    grid = []
    for line in fileinput.input():
        line = line.strip()
        if not line:
            break
        grid.append(list(line))

    pprint(grid)

    count = 0
    my_grid = Grid(grid)
    for rolls in my_grid:
       # print(rolls)
        _, x, y = rolls
        result = my_grid.neighbors_count(x,y)

        if result < 4:
            count += 1
            print(f"{x},{y} --> {result }")

    print(count)


if __name__ == "__main__":
    main()
