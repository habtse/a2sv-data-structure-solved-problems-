class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) 
        while low < high:
            print(low,high)
            mid = low + (( high  - low ) // 2)
            if target > nums[mid]:
                low = mid + 1           
            elif target < nums[mid]:
                high = mid 
            elif target == nums[mid]:
                return mid
            
        return -1
            
            