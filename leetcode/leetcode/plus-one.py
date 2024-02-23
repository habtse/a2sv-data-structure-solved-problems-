class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        strList = [str(i) for i in digits]
        intValue = int(''.join(strList))+1
        output =deque([])
        while intValue:
            output.appendleft(intValue%10)
            intValue = intValue//10
        return output