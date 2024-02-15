class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic ={}
        count = 0
        for i in s:
            if  i in dic:
                dic[i]+=1
            else:
                dic[i] =1
        for i in dic:
            if dic[i] > 1:
                if dic[i] % 2 ==0:
                    count +=dic[i]
                else:
                    count += dic[i]-1
        if count < len(s):
            count +=1
        return count

            
