class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        total =0
        curr = nums[-1]
        for i in range(len(nums)-2,-1,-1):
            
            total += ceil(nums[i]/curr)-1

            if curr> nums[i]:
                curr = nums[i]
            elif nums[i]%curr ==0:
                curr = curr
            else:

                curr = nums[i]//ceil(nums[i]/curr)

            
            
        return total

