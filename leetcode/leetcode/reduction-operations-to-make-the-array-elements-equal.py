class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        count =0
        index =0
        output = 0
        for i in range(1,len(nums)):
            if nums[index] != nums[i]:
                count +=1
                output  += count
                index = i
            elif nums[0] != nums[i]:
                output +=count
        return output



