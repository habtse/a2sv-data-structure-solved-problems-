class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        minValue = float('inf')
        maxValue = float('-inf')
        for i in nums:
            if i > maxValue:
                maxValue = i
            if i <minValue:
                minValue = i
        # print(minValue,maxValue)
        if maxValue - minValue > 2*k:
           return maxValue - minValue - 2*k
        else:
            return 0