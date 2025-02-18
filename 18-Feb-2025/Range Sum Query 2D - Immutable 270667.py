# Problem: Range Sum Query 2D - Immutable - https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):

        for i in range(len(matrix)):
            for j in range(1, len(matrix[0])):
                matrix[i][j] += matrix[i][j-1]

        for j in range(len(matrix[0])):
            for i in range(1, len(matrix)):
                matrix[i][j] += matrix[i-1][j]
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        top_subtract = left_subtract = diagonal_add = 0
        if row1-1 > -1:
            top_subtract = self.matrix[row1-1][col2]
        if col1-1 > -1:
            left_subtract = self.matrix[row2][col1-1]
        if row1-1 > -1 and col1-1 > -1:
            diagonal_add = self.matrix[row1-1][col1-1]
        return self.matrix[row2][col2] - top_subtract - left_subtract + diagonal_add       


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)