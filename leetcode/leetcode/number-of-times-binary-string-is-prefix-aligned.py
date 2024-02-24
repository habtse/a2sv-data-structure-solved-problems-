class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        highest =0
        count =0
        for i in range(len(flips)):
            if flips[i] > highest:
                highest =flips[i]
            if highest == i+1:
                count +=1
        return count

        