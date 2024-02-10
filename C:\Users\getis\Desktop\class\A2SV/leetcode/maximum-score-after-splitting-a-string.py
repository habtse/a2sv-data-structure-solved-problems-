class Solution:
    def maxScore(self, s: str) -> int:
        prefix_sum_1 = []
        prefix_sum_0 = []
        total1=0
        total0=0
        for i in s:
            if i =='0':
                total0 +=1
            if i == '1':
                total1 +=1
            prefix_sum_0.append(total0)
            prefix_sum_1.append(total1)
        length = len(prefix_sum_0)
        output=0
        maximum_sum = float('-inf')
        for i in range(length-1):
            output = (prefix_sum_1[length-1]-prefix_sum_1[i]+prefix_sum_0[i])
            maximum_sum = max(output,maximum_sum)
        return maximum_sum

