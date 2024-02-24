class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        count = 0
        for i in range(len(mat))  :              
            count += mat[i][i]
            if i !=len(mat)-1-i:
                count+= mat[i][len(mat)-1-i]
        return count
