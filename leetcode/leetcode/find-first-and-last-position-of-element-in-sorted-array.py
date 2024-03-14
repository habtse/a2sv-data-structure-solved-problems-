class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low, high = 0, len(nums) - 1
        if len(nums) == 1:
            if nums[low] == target:
                return [0,0]
            
        # if not nums:
        #     return ans = [-1,-1]
        ans = [-1,-1]
        tag = False
        prevHigh = len(nums) - 1
    
        while low < high:
            mid = low + ((high - low)// 2)
            if target > nums[mid]:
                low = mid + 1
            elif target < nums[mid]:
                high = mid
                prevHigh = mid
            else:                
                high = mid
            if high == low and nums[low] == target:
                ans[0] = low
                tag = True
        if tag:
            high = prevHigh
            if nums[high] == target:
                ans[-1] = high
                return ans
            while low < high:
                mid = low + ((high - low)// 2)
                if target == nums[mid]:
                    low = mid + 1
                else:
                    high = mid
            ans[-1] = high - 1
        
        return ans


