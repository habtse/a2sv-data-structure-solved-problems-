class Solution:
    def decodeString(self, s: str) -> str:

        # number = 0
        # count_open = 0
        # count_close = 0
        # decoded = []
        # left = 0

        # for right in range(len(s)) :
        #     if s[right].isdigit():
        #         number = int(s[right])
        #     elif s[right] == '[':
        #         count_open += 1
        #         if count_open == 1:
        #             left = right
        #     elif s[right] == ']':
        #         count_close += 1
        #         if count_close == count_open:
        #             decoded = number * self.decodeString(s[left + 1: right])

        #     elif count_open ==0:
        #         return list(s)
        #     else:
        #         decoded.append
        # return ''.join(decoded)

        def rec(s):

            if '[' not in s:
                return s
            
            left_bracket_index = s.index('[')
            right_bracket_index = -1
            
            n_open = 1
            for i in range(left_bracket_index+1, len(s)):
                if s[i] == '[':
                    n_open += 1
                elif s[i] == ']':
                    n_open -= 1
                
                if n_open == 0:
                    right_bracket_index = i
                    break
            
            n_index = 0
            for j in range(left_bracket_index):
                if s[j].isdigit():
                    n_index = j
                    break
            
            s1 = s[:n_index]
            n = int(s[n_index:left_bracket_index])
            s2 = s[left_bracket_index+1: right_bracket_index]
            s3 = s[right_bracket_index+1:]
        
            return rec(s1) + n*rec(s2) + rec(s3)
        return rec(s)


            

            

            
        