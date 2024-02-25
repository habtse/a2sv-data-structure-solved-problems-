class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        total =0
        index =0
        while index < len(costs) and total <= coins:
            total += costs[index]
            index +=1
        if index ==len(costs) and total < coins:
            return index
        return index -1
            