import numpy as np


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        mainGrid = np.array(grid)
        transpose = mainGrid.transpose()
        summ = 0
        print(transpose)
        for x in range(len(mainGrid)):
            
            for y in range(len(mainGrid[x])):
                currVal = min(max(mainGrid[x]),max(transpose[y]))
                summ += currVal-mainGrid[x][y] 
        return summ
