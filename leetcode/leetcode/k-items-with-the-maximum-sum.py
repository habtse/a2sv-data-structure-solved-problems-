class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        total = 0
        requiredZero =0
        requiredNeg =0
        if k> numOnes:
            total += numOnes 
            requiredZero = k-numOnes
        if requiredZero > numZeros:
            requiredNeg = requiredZero - numZeros
            total += (requiredNeg *-1)
        if k <= numOnes:
            total += k
        return total