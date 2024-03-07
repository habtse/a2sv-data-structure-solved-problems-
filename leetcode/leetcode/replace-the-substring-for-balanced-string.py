class Solution:
    def balancedString(self, s: str) -> int:
        def isBalanced(n,dic):
            for i in dic.values():
                if i > n :
                    return False
            return True

        dic = {}
        n = len(s)//4
        for i in s:
            dic[i] = dic.get(i,0) + 1
        if isBalanced(n,dic):
            return 0
        left = 0
        result = float('inf')
        for right in range(len(s)):
            dic[s[right]] -= 1

            while left <= right and isBalanced(n,dic):
                result = min(result,right-left+1)
                dic[s[left]] +=1
                left +=1
            
        return result
        
