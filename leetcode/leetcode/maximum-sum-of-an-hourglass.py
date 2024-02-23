class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        firstPrefix=[[0]*(len(grid[0])+1)]
        for i in range(len(grid)):
            prefix =[0]
            for j in range(len(grid[i])):
                prefix.append(prefix[-1]+ grid[i][j])
            firstPrefix.append(prefix)
        
        secondPrefix=[]
        for x in range(1,len(firstPrefix)):
            for y in range(len(firstPrefix[x])):
                firstPrefix[x][y] +=firstPrefix[x-1][y]
        print(firstPrefix)
        max_sum = float('-inf')
        for row in range(3,len(firstPrefix)):
            for column in range(3,len(firstPrefix[0])):
                max_sum = max(max_sum,firstPrefix[row][column]+firstPrefix[row-3][column-3]-firstPrefix[row-3][column]-firstPrefix[row][column-3]-grid[row-2][column-1]-grid[row-2][column-3])
        return max_sum


            