from collections import deque
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque([])
        count = len(tickets)
        if tickets[k] ==1:
            return k+1
        for i in range(len(tickets)):
            if tickets[i]-1 !=0:
                queue.append((tickets[i]-1,i))
        
        while True:
            n = queue.popleft()
            if n[1] == k and n[0]==1:
                return count+1
            count +=1
            if n[0] !=1:
                queue.append((n[0]-1,n[1]))


