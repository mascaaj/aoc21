""" Puzzle for day15 advent of code 2021
"""
import numpy as np
import heapq


# windows filepath
filename = '..\data\data.txt'
input_map = np.empty(0)


class BasinFinder():
    def __init__(self, matrix):
        self.matrix = matrix
        self.dest = (self.matrix.shape[0]-1, self.matrix.shape[1]-1)
        self.move_x = [1, 0, -1, 0]
        self.move_y = [0, 1, 0, -1]
        self.visited = np.zeros(shape=(self.matrix.shape[0], self.matrix.shape[1]))
        self.min_distance = float('inf')
        self.low_point_array = []
        self.low_point_location = []

    def is_valid(self, row, col, visited):
        dims = self.matrix.shape
        if row < 0 or row >= dims[0]:
            return False
        if col < 0 or col >= dims[1]:
            return False
        if not self.matrix[row, col]:
            return False
        if (row, col) in visited:
            return False
        return True

# Begin modelling arount G(V,E)
    def solve(self, start_i, start_j):
        listname = [(0, (start_i, start_j))]
        visited = set()
        while listname:
            current_distance, current_location = heapq.heappop(listname)
            if current_location in visited:
                continue
            visited.add(current_location)
            if current_location == self.dest:
                self.min_distance = current_distance
            for move in range(len(self.move_x)):
                next_i = current_location[0] + self.move_x[move]
                next_j = current_location[1] + self.move_y[move]
                if self.is_valid(next_i, next_j, visited):
                    distance = current_distance + self.matrix[next_i, next_j]
                    heapq.heappush(listname, (distance, (next_i, next_j)))

    def show_result(self):
        if self.min_distance != float("inf"):
            print("shortest path : ", self.min_distance)


def convert_string_to_list(string):
    list1 = []
    list1[:0] = string
    return list1


def read_data(file):
    input_map = []
    with open(file) as fn:
        lncount = 0
        ln = fn.readline()
        while ln:
            ln = convert_string_to_list(ln.strip("\n"))
            lnwidth = len(ln)
            input_map = np.append(input_map, ln)
            ln = fn.readline()
            lncount += 1
    return input_map, lncount, lnwidth


if __name__ == "__main__":
    input_map, lncount, lnwidth = read_data(filename)
    input_map = input_map.astype(int).reshape(lncount, lnwidth)
    map = BasinFinder(input_map)
    map.solve(0, 0)
    result = map.min_distance
    print(result)
