class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left = 0
        right = 0
        if len(nums) == 1 or total - nums[0] == left:
            return 0
        for i in range(1,len(nums)):
            left +=nums[i-1]
            right = total -nums[i] -left
            if left == right:
                return i
        return -1

