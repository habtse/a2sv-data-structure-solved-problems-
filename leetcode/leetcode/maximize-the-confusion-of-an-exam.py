class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        check = 'T'
        left = 0
        count = 0
        result =0
        #  CALCULATE FOR answerKey[0]
        for right in range(len(answerKey)):
            if answerKey[right] != check:
                count += 1
            while count > k:
                count -=1 if answerKey[left] == answerKey[right] else 0
                left +=1
            result = max(result,right-left+1)
        # CALCULATE FOR not answerKey[0]]
        check = 'F'
        left = 0
        count = 0
        for right in range(len(answerKey)):
            if answerKey[right] != check:
                count += 1
            while count > k:
                count -=1 if answerKey[left] == answerKey[right] else 0
                left +=1
            result = max(result,right-left+1)
        return result
        

        