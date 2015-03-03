#!/usr/bin/env python

import sys
import time

BUFFER = 5
DEAD_CHAR = '.'
FILL_CHAR = ' '
INTERVAL = 0.05

class Life:

    def __init__(self, seed_file):
        self.live_char = None
        self.dead_char = DEAD_CHAR
        self.parse_seed(seed_file)

    def num_neighbours(self, row, col):
        num_neighbours = 0
        neighbour_indices = [(row - 1, col - 1), (row - 1, col),
                (row - 1, col + 1), (row, col - 1), (row, col + 1),
                (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)]
        for (row, col) in neighbour_indices:
            try:
                num_neighbours += self.grid[row][col]
            except IndexError:
                pass
        return num_neighbours

    def cell_next_gen(self, row, col):
        num_neighbours = self.num_neighbours(row, col)
        if self.grid[row][col] == 1:
            if num_neighbours < 2:
                return 0
            if num_neighbours > 3:
                return 0
            return 1
        if num_neighbours == 3:
            return 1
        return 0

    def next_gen(self):
        new_grid = []
        for row in range(len(self.grid)):
            new_grid.append([])
            for col in range(len(self.grid[0])):
                new_grid[row].append(self.cell_next_gen(row, col))
        self.grid = new_grid

    def print_grid(self):
        """ Print the grid to the screen. """

        def make_horizontal_border(width, corner_char, border_char):
            """ Generates a nice horizonal border for the grid. """
            border = corner_char
            for col in range(width):
                border = border + border_char
            border = border + corner_char
            return border

        hor_border = make_horizontal_border(len(self.grid[0]) - BUFFER * 2,
                '+', '-')

        print hor_border
        for row in range(BUFFER, len(self.grid) - BUFFER):
            row_str = '|'
            for col in range(BUFFER, len(self.grid[0]) - BUFFER):
                if self.grid[row][col] == 0:
                    row_str = row_str + FILL_CHAR
                else:
                    row_str = row_str + self.live_char
            print row_str + '|'
        print hor_border

    def make_empty_grid(self, rows, cols):
        return [[0 for col in range(cols)] for row in range(rows)]

    def parse_seed(self, seed_file):
        with open(seed_file, 'r') as seed:
            lines = seed.readlines()
        self.grid = self.make_empty_grid(len(lines) + BUFFER * 2,
                len(lines[0]) + BUFFER * 2)

        for row in range(len(lines)):
            for col in range(len(lines[row].strip())):
                char = lines[row][col]
                if char != self.dead_char:
                    if self.live_char is None:
                        self.live_char = char
                    if char == self.live_char:
                        self.grid[row + BUFFER][col + BUFFER] = 1
                    else:
                        print self.live_char
                        raise ValueError('Unknown character in seed file, '
                                '<{}>.'.format(char))

def main():
    seed_file = sys.argv[1]
    life = Life(seed_file)

    while True:
        print(chr(27) + "[2J") # Scary escape sequence to clear the terminal.
        print "Conway's Game of Life"
        life.print_grid()
        life.next_gen()
        time.sleep(0.1)

if __name__ == '__main__':
    main()
