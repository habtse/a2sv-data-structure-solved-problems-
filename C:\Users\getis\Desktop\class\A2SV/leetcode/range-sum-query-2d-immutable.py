class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.row_add_matrix = []
        self.column_add_matrix=[]
        self.no_column = len(self.matrix[0])
        self.no_row = len(self.matrix)
        self.first = [0]*(self.no_column +1)
        self.row_add_matrix.append(self.first)

        for row in self.matrix:
            self.row_prefix_sum =[0]
            total = 0
            for element in row:
                total +=element
                self.row_prefix_sum.append(total)
            self.row_add_matrix.append(self.row_prefix_sum)
        self.column_add_matrix.append(self.row_add_matrix[0])
        # print(self.column_add_matrix)
        for i in range(1,self.no_row+1):
            self.column_prefix_sum =[]
            total = 0
            for j in range(self.no_column+1):
                total = self.column_add_matrix[i-1][j] + self.row_add_matrix[i][j]
                self.column_prefix_sum.append(total)
            self.column_add_matrix.append(self.column_prefix_sum)
        
                




    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        output = self.column_add_matrix[row2+1][col2+1]-self.column_add_matrix[row1][col2+1] - self.column_add_matrix[row2+1][col1] + self.column_add_matrix[row1][col1]
        return output

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)