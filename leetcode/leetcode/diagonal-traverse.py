class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        dic = {}
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if i+j in dic:
                    dic[i+j].append(mat[i][j])
                else:          
                    dic[i+j] =[mat[i][j]]
        output =[]
        for i in range(len(dic))  :
            if i%2 ==0:
                for j in range(len(dic[i])-1,-1,-1):
                    output.append(dic[i][j])
            else:
                for j in range(len(dic[i])):
                    output.append(dic[i][j])
        return output

