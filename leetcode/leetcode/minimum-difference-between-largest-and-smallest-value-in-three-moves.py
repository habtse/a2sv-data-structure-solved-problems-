class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) <5:
            return 0
        firstCase = (nums[-1]-nums[3])
        secondCase = (nums[-2]-nums[2])
        thirdCase = (nums[-3]-nums[1])
        fourthCase = (nums[-4]-nums[0])
        
        
        return min(firstCase , secondCase, thirdCase, fourthCase )