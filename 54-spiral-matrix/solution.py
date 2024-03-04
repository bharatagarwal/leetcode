"""
Given an m x n matrix, return all elements of the matrix in spiral order.
                  . . .   | | *   & & *
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""

def rotate_counter(matrix):
    rows, cols = len(matrix), len(matrix[0])

    new = []
    for _ in range(cols):
        new.append([])

    for col in range(cols):
        for row in range(rows):
            new[col].append(matrix[row][cols - 1 - col])

    return new

class Solution:
    def spiralOrder(self, matrix):
        new = []

        while len(matrix) > 0:
            new.extend(matrix.pop(0))

            if len(matrix) == 0:
                continue

            matrix = rotate_counter(matrix)

        return new
