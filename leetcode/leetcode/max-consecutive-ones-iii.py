class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        count_zero = 0
        left = 0
        result = 0
        for right in range(len(nums)):
            count_zero += 1 if nums[right] == 0 else 0
            while count_zero > k:
                count_zero -=1 if nums[left] == 0 else 0
                left += 1
            result = max(result, right-left+1)
        return result

        