class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low, high = max(weights), sum(weights)
        def canShipAll(capacity):
            passed_day = 1
            cur_weight = 0
            for i in range(len(weights)):
                cur_weight += weights[i]
                
                if cur_weight > capacity:
                    passed_day += 1
                    cur_weight = weights[i]
                
                if passed_day > days:
                    return False
            return True
        while low < high:
            mid = low + ((high - low ) // 2)
            if canShipAll(mid):
                high = mid
            else:
                low = mid + 1
        return low

            
                    
