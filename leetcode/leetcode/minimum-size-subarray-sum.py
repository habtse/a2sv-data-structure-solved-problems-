class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        value = 0
        min_len = len(nums)
        start = 0
        if sum(nums)< target:
            return 0
        for i in range(len(nums)):
            value +=nums[i]
            while value >= target:
                value -=nums[start]
                min_len = min(min_len,i - start+1)
                start +=1
        return min_len

            