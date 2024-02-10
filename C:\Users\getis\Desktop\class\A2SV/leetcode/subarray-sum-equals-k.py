class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total = 0
        visited = {0:1}
        count=0
        for i in nums:
            total += i 
            if total -k in visited:
                count +=visited[total-k]
            visited[total] = visited.get(total,0)+1
        
        return count
        
