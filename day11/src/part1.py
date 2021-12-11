""" Puzzle for day11 advent of code 2021
"""
import numpy as np
import collections


# windows filepath
filename = '..\data\sample.txt'
input_array = np.empty(0)


class FlashFinder():
    def __init__(self, matrix):
        self.matrix = matrix
        self.move_x = [1, 0, -1, 0, 1, 1, -1, -1]
        self.move_y = [0, 1, 0, -1, 1, -1, 1, -1]
        self.visited = np.zeros(shape=(self.matrix.shape[0], self.matrix.shape[1]))
        self.count = 0

    def is_valid(self, row, col):
        dims = self.matrix.shape
        if row < 0 or row >= dims[0]:
            return False
        if col < 0 or col >= dims[1]:
            return False
        if not self.matrix[row, col]:
            return False
        if self.visited[row, col]:
            return False
        return True

    def solve(self, start_i, start_j):
        self.matrix[start_i][start_j] = 0
        self.count += 1
        queue = collections.deque()
        queue.append((start_i, start_j))
        while queue:
            (i, j) = queue.popleft()
            self.reset_visited()
            for move in range(len(self.move_x)):
                next_x = i + self.move_x[move]
                next_y = j + self.move_y[move]
                if self.is_valid(next_x, next_y):
                    self.visited[next_x, next_y] = 1
                    if not self.matrix[next_x, next_y] == 0:
                        self.matrix[next_x, next_y] += 1

    def get_min_cells(self):
        return self.count

    def find_ripe(self):
        locations = np.where(self.matrix >= 10)
        self.location_array = collections.deque(sorted(list(zip(locations[0], locations[1]))))

    def step(self):
        self.matrix = self.matrix+1

    def reset_visited(self):
        self.visited = np.zeros(shape=(self.matrix.shape[0], self.matrix.shape[1]))


def convert_string_to_list(string):
    list1 = []
    list1[:0] = string
    return list1


# line read
with open(filename) as fn:
    lnheight = 0
    ln = fn.readline()
    while ln:
        ln = convert_string_to_list(ln.strip("\n"))
        input_array = np.append(input_array, ln)
        lnwidth = len(ln)
        lnheight += 1
        ln = fn.readline()
    input_array = input_array.astype(int).reshape(lnheight, lnwidth)
    flash = FlashFinder(input_array)
    for k in range(1, 101):
        print(k)
        flash.step()
        flash.find_ripe()
        if flash.location_array:
            while flash.location_array:
                flashloc = flash.location_array.popleft()
                flash.solve(flashloc[0], flashloc[1])
                flash.find_ripe()
        print(flash.matrix)
print(flash.count)
