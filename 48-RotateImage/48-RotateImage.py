from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i,n):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

        for i in range(n):
            matrix[i].reverse()
        return

if __name__ == "__main__":
    matrix = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
    soln = Solution()
    soln.rotate(matrix)

        