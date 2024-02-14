class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        ls =[]
        for i in range(len(costs)) :
            a,b = costs[i]
            ls.append([a-b,i])
        ls.sort(key=lambda x : x[0])
        total =0
        leng = len(costs)-1
        for j in range(len(costs)//2):
            total += costs[ls[j][1]][0] +costs[ls[leng-j][1]][1]
        return total
        