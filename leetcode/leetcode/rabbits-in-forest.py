class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        dic = {}
        count =0
        for i in answers:
            if i in dic:
                dic[i] +=1
            else:
                dic[i] =1
        for i in dic:
            print (i,dic[i])
            count +=ceil(dic[i]/(i+1 ) )*(i+1)
        return count
