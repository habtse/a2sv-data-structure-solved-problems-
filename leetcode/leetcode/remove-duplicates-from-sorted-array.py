class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # sett = list(set(nums))
        dic ={}
        count =-1
        for i in range(len(nums)):
            if nums[i] in dic.values():
                continue
            else:
                count +=1
                dic[count] = nums[i]


        # print(sett)
        # expectedNums =[]
        for i in range(len(nums)):
            if i in dic:
                nums[i]=dic[i]
            else:
                nums[i] = '_'
        return len(dic)
