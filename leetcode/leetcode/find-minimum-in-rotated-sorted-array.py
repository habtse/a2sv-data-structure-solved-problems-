class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) -1
        target = nums[0]
        if nums[low] < nums[-1]:
            return nums[low]

        while low < high:
            mid = low + ((high - low ) // 2)
            if nums[mid] >= target:
                low = mid + 1
            elif nums[mid]< target:
                high = mid
        return nums[low]