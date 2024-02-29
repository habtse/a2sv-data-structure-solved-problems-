class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if len(cardPoints)==k:
            return sum(cardPoints)
        count = 0
        left, right = 0,len(cardPoints)-1
        ls = deque(cardPoints[len(cardPoints)-k:])
        total = sum(ls)
        result = sum(ls)
        for i in range(len(cardPoints[:k])):
            poped = ls.popleft()
            ls.append(cardPoints[i])
            total =total-poped+ cardPoints[i]
            result  = max(result,total)
        return result
        # while count < k:
        #     if cardPoints[left] > cardPoints[right]:
        #         result += cardPoints[left]
        #         left += 1
        #     elif cardPoints[left] < cardPoints[right]:
        #         result += cardPoints[right]
        #         right -= 1
        #     else:
        #         localLeft = left
        #         localRight = right
        #         while cardPoints[localLeft] == cardPoints[localRight] and count < k :
        #             localLeft +=1
        #             localRight -=1
        #             count += 1
        #         if cardPoints[left] > cardPoints[right]:
        #             result += cardPoints[left]
        #             left += 1
        #         elif cardPoints[left] < cardPoints[right]:
        #             result += cardPoints[right]
        #             right -= 1


