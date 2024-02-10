class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        lst = list(s)
        ls= [0]*(len(s)+1)
        for  begin,end,direction in shifts:
            if direction ==0:
                ls[begin]  -=1   
                ls[end+1]  +=1
            else:
                ls[begin]  +=1   
                ls[end +1]  -=1
        cum_sum = 0
        for i in range(len(s)):
            cum_sum += ls[i]
            
            new_code = (((ord(s[i]) + cum_sum) - 97) % 26) + 97
            s = s[:i] + chr(new_code) + s[i+1:]
        
        return s


        #     for i in range(begin, end +1):
        #         ord_i = ord(lst[i])
                
        #         if direction == 0:
        #             ord_i = ord_i -1
        #             if ord_i ==96:
        #                 ord_i = 122
        #         else:
        #             ord_i = ord_i +1
        #             if ord_i == 123:
        #                 ord_i = 97
        #         new_char = chr(ord_i)
        #         lst[i] = new_char
        # return ''.join(lst)

            