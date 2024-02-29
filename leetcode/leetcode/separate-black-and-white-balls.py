class Solution:
    def minimumSteps(self, s: str) -> int:
        total = 0
        result = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] == '1':
                result +=total
            else:
                total +=1
        return result
