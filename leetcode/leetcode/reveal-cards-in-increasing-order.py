class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        queue = deque([])
        n = len(deck)
        for i in range(n-1,-1,-1):
            lastValue = deck[i]
            # print(lastValue)
            if queue:
                popedVal =queue.pop()
                queue.appendleft(popedVal)
            queue.appendleft(lastValue)
        return queue

        
        # output =[]
        # for i in range((n+1)//2):
        #     output.append(deck[i])
        #     if (n+1)//2+i < n:
        #         output.append(deck[(n+1)//2+i])
        # return output