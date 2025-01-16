class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        zeros = []
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == 0:
                    zeros.append((row, col))
        for row, col in zeros:
            for j in range(len(matrix)):
                matrix[j][col] = 0
            for k in range(len(matrix[0])):
                matrix[row][k] = 0


