class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        dic = {}
        ls = []
        total = 0
        result = float('-inf')
        for i in range(len(nums)):
            
            if nums[i] in ls:
                ls =ls[ls.index(nums[i])+1:]
                total = sum(ls) + nums[i]   
                
            else:
                total += nums[i]            
                dic[nums[i]] = i+1
            ls.append(nums[i])
            result = max(result,total)
        return result