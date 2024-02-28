class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        average = sum(nums[:k])/k
        output = sum(nums[:k])/k
        index = 0
        for i in range(k,len(nums)):
            average += (nums[i]-nums[index])/k 
            output = max(output, average  )
            index += 1
        return output