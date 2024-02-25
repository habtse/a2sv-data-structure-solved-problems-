class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        steps = len(piles)//3
        result = 0

        for i in range(steps):
            result +=piles[-(i*2 +2)]
        return result

