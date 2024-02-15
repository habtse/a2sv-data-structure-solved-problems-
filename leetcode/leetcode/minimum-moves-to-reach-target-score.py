class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        currDouble = maxDoubles
        currTarget = target
        count =0
        while currDouble >0 and currTarget >1:
            if currTarget % 2 ==1:
                count+=1
            currTarget //=2 
            count +=1
            currDouble -=1
        count += currTarget-1
        return count