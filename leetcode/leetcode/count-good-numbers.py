class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9+7
        if n %2 ==1:
           return (pow(20,n//2,MOD)*5)%(10**9+7)
        else:
            return pow(20,n//2,MOD)%(10**9+7)