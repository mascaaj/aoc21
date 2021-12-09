""" Puzzle for day9 advent of code 2021
"""
import numpy as np
import collections

# windows filepath
filename = '..\data\data.txt'
input_map = np.empty(0)
basins = []


class BasinFinder():
    def __init__(self, matrix):
        self.matrix = matrix
        self.move_x = [1, 0, 0, -1]
        self.move_y = [0, -1, 1, 0]
        self.visited = np.zeros(shape=(self.matrix.shape[0], self.matrix.shape[1]))
        self.min_distance = float('inf')
        self.low_point_array = []
        self.low_point_location = []

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
        if self.matrix[row, col] == 9:
            return False
        return True

    def solve(self, start_i, start_j):
        self.matrix[start_i][start_j] = True
        count = 0
        queue = collections.deque()
        queue.append((start_i, start_j, 0))

        while queue:
            (i, j, dist) = queue.popleft()
            count += 1
            for move in range(len(self.move_x)):
                next_x = i + self.move_x[move]
                next_y = j + self.move_y[move]
                if self.is_valid(next_x, next_y):
                    self.visited[next_x, next_y] = 1
                    queue.append((next_x, next_y, dist + 1))
        self.min_distance = count

    def get_min_cells(self):
        return self.min_distance

    def test_min(self):
        for i in range(self.matrix.shape[0]):
            for j in range(self.matrix.shape[1]):
                flag = 0
                tv = self.matrix[i, j]
                t1, t2, t3, t4 = -1, -1, -1, -1
                if i - 1 >= 0:
                    t1 = self.matrix[i - 1, j]
                if i + 1 < self.matrix.shape[0]:
                    t2 = self.matrix[i + 1, j]
                if j - 1 >= 0:
                    t3 = self.matrix[i, j - 1]
                if j + 1 < self.matrix.shape[1]:
                    t4 = self.matrix[i, j + 1]
                test_list = [tv, t1, t2, t3, t4]
                if test_list.count(-1) > 0:
                    test_list.remove(-1)
                if test_list.count(-1) > 0:
                    test_list.remove(-1)
                for k in range(1, len(test_list)):
                    if test_list[0] >= test_list[k]:
                        flag = 1
                if not flag:
                    self.low_point_array.append(test_list[0])
                    self.low_point_location.append((i, j))


def convert_string_to_list(string):
    list1 = []
    list1[:0] = string
    return list1


# line read
with open(filename) as fn:
    lncount = 0
    ln = fn.readline()
    while ln:
        ln = convert_string_to_list(ln.strip("\n"))
        lnwidth = len(ln)
        input_map = np.append(input_map, ln)
        ln = fn.readline()
        lncount += 1
    input_map = input_map.astype(int).reshape(lncount, lnwidth)
    map = BasinFinder(input_map)
    map.test_min()
    for i in map.low_point_location:
        map.solve(i[0], i[1])
        basins.append(map.get_min_cells()-1)
    candidate = sorted(basins)
    print(candidate[-3] * candidate[-2] * candidate[-1])
