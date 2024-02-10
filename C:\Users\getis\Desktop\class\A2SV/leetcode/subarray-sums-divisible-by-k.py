class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dic = {0:1}
        total =0
        count =0
        for i in nums:
            total +=i
            if total%k in dic:
                count +=dic[total%k]
                dic[total%k] +=1
            else:
                dic[total%k] = 1
        return count