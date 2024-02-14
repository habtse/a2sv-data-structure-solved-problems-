class Solution:
    def canJump(self, nums: List[int]) -> bool:
        j = len(nums)-1
        i = len(nums)-2
        while j >= 1 and i>=0:
            if i == 0 and j>nums[i]+i:
                return False
            if i + nums[i] >= j:
                j=i
                i-=1
            else:
                i-=1
        return True