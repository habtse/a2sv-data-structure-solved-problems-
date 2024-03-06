# class Solution:
#     def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
#         count = 0
        
#         for i in range(len(matrix)):
#             for j in range(1,len(matrix[0])):
#                 if matrix[i][j] == target:
#                     count += 1             

#                 matrix[i][j] += matrix[i][j-1]
#                 if matrix[i][j] == target: 
#                     count +=1
#                 k = j-2
#                 while k >= 0  :
                     
#                     if matrix[i][j] - matrix[i][k] == target: 
#                         count +=1
#                     k -= 1
#         for i in range(1,len(matrix)):
#             for j in range(len(matrix[0])):

#                 matrix[i][j] +=  matrix[i-1][j]
                
#                 if matrix[i][j] == target: 
#                     count +=1
#                 k = i-1
#                 while k >= 0  :
#                     if j == 0 and k > 0 and matrix[i][j] - matrix[k][j] == target:
#                         count += 1
#                     elif i-k == 1 and j > 0 and i == 1:
#                         if  matrix[i][j] - matrix[i][j-1] == target:
#                             count +=1
#                         k-=1
#                         continue
#                     elif i-k == 1 and j > 0 :
#                         if  matrix[i][j] - matrix[k][j] - matrix[i][j-1] + matrix[k][j-1] == target:
#                             count +=1
#                         k -=1 
#                         continue
                        
#                     elif  matrix[i][j] - matrix[k][j] - matrix[i][j-1] + matrix[k][j-1] == target: 
#                         count +=1
                    
#                     k -= 1
                    
            
#         for i in range(1,len(matrix)):
#             for j in range(1,len(matrix[0])):
#                 k = i-2
#                 l = j - 2
#                 while k >= 0  :
#                     if l == -1 and matrix[i][j] - matrix[k][j] == target:
#                         count += 1
                        
#                     if l > -1 and matrix[i][j] - matrix[k][j] - matrix[i][l] + matrix[k][l]== target: 
#                         count += 1
#                     l -=1
#                     if l > -1 and matrix[i][j] - matrix[k][j] - matrix[i][l] + matrix[k][l]== target:
#                         count +=1
#                     l += 1
#                     k-=1
#                     if j > -1 and matrix[i][j] - matrix[k][j] - matrix[i][l] + matrix[k][l]== target:
#                         count +=1
                    
#                     l -= 1




        
#         return count
        

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        n=len(matrix)
        m=len(matrix[0])
        ans=0
        for r in matrix:
            for i in range(1,len(r)):
                r[i]+=r[i-1]
        for start in range(m):
            for end in range(start,m):
                lookup=defaultdict(int)
                cumsum=0
                lookup[0]=1
                for k in range(n):
                    cumsum+=matrix[k][end] - (matrix[k][start-1] if start !=0 else 0)
                    if cumsum -target in lookup:
                        ans+=lookup[cumsum-target]
                    lookup[cumsum]+=1
        return ans                        