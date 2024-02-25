class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortednums = nums.copy()
        sortednums.sort()
        dic ={}
        output =[]
        for i in range(len(sortednums)):
            if sortednums[i] not in dic:
                dic[sortednums[i]]= i
        for i in nums:
            output.append(dic[i])
        return output

