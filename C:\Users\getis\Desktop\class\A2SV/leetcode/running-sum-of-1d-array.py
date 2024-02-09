class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ls = []
        total =0
        for i in nums:
            total +=i
            ls.append(total )
        return ls