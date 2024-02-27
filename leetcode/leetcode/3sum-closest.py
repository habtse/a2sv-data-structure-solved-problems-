class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest = float('inf')
        output = 0
        for i in range(n-2):
            j = i+1
            k = n-1
            
            while j<k:
                if nums[i]+nums[j]+ nums[k] ==target:    
                    print(True)                
                    return target

                if abs(nums[i]+nums[j]+ nums[k]-target) <=closest:
                    output =nums[i]+nums[j]+ nums[k]
                    closest = abs(nums[i]+nums[j]+ nums[k]-target)
                if nums[i]+nums[j]+ nums[k]>target:
                    k-=1
                else:


                    j+=1

        return output