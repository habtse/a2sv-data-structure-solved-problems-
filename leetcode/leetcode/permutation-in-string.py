from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1_len = len(s1)        
        if s1_len > len(s2):
            return False

        answer_key, fixed_size_window = Counter(s1), Counter(s2[:s1_len])
        print (answer_key)

        for idx, char in enumerate(s2[s1_len:], start=s1_len):
            if fixed_size_window == answer_key:
                return True 
            
            start_char = s2[idx-s1_len]
            
            fixed_size_window[start_char] -= 1
            fixed_size_window[char] += 1

            if fixed_size_window[start_char] == 0:
                del fixed_size_window[start_char]
        
        return fixed_size_window == answer_key