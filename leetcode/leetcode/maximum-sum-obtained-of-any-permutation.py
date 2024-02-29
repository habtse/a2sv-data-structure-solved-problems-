class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        initial =[0]*(len(nums)+1)
        nums.sort()
        for a,b in requests:
            initial[a] +=1
            initial[b+1] -=1
        total =0
        initial_d =[0]*(len(nums))
        for i in range(len(initial_d)):
            total +=initial[i]
            initial_d[i] =total
        

        initial_d.sort()
       
        total_2 =0
        for i in range(len(nums)):
            total_2 = total_2 + (initial_d[i] * nums[i])
        return (total_2 % (10**9+7)) 



        