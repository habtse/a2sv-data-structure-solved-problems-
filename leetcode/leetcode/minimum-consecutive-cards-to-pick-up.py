class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        dic = {}
        result = float('inf')
        for i in range(len(cards)):
            if cards[i] in dic:
                
                result = min(i - dic[cards[i]] + 1,result)
                dic[cards[i]] = i               
            else:
                dic[cards[i]] = i
        if result == float('inf'):
            return -1
        return result