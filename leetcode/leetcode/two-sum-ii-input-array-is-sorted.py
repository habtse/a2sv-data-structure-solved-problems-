class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left ,right = 0,len(numbers)-1
        for i in range (len(numbers)):
            if numbers[right]+numbers[left] == target:
                return [left+1,right+1]
            elif numbers[right]+numbers[left] < target:
                left +=1
            else: 
                right -=1
        