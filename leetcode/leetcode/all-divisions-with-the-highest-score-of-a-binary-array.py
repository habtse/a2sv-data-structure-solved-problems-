class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        # count  0 from the beginning
        prefix = [0]
        # count 1 from the end
        suffix = [0]
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                prefix.append(prefix[i]+1)
            else:
                prefix.append(prefix[i])
            if nums[n-i-1] == 0:
                suffix.append(suffix[i])
            else:
                suffix.append(suffix[i]+1)
        maxSum = 0
        output = []
        for i in range(n+1):
            if prefix[i]+suffix[n-i] > maxSum:
                maxSum =prefix[i]+suffix[n-i]
                output=[]
                output.append(i)
            elif prefix[i]+suffix[n-i] == maxSum:
                
                output.append(i)
        return output

        