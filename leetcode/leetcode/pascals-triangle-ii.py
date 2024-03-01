class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = []
        def calculate(rowIndx):
            row = [1]
            if rowIndx <2:
                return [1]*(rowIndx+1)
            # print(rowIndx-1)
            output = calculate(rowIndx-1)
            for i in range(1,len(output)):
                row.append(output[i-1]+output[i])
            row.append(1)
            return row
        return calculate(rowIndex)
            



