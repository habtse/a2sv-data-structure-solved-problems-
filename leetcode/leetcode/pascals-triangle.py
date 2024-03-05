class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows < 2:
            return [[1]]
        output = [[1]]
        
        for i in range(1,numRows ):
            output.append([1])
            for j in range(1,len(output[i-1])):
                output[i].append(output[i-1][j-1] + output[i-1][j])
            output[i].append(1)
        return output

            

