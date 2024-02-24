class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i):
                matrix[j][i], matrix[i][j] = matrix[i][j],matrix[j][i]
        for i in matrix:
            for j in range(len(matrix)//2):
                i[j],i[len(matrix)-1-j] =i[len(matrix)-1-j],i[j]
        return matrix

