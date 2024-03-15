class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def possible(k):
            hour_take = 0
            for bananas in piles:
                hour_take += ceil(bananas/k)
                if hour_take > h:
                    return False
            return True
        low, high = 1,sum(piles)
        while low < high:
            mid = (low + high) // 2
            if possible(mid) :
                high = mid
            else:
                low = mid + 1
        return low