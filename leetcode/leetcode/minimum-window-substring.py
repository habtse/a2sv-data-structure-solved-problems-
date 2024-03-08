# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         if not s or not t or len(s) < len(t):
#             return ''
#         t_count = {}
#         for char_t in t:
#             t_count[char_t] = t_count.get(char_t,0) + 1

#         def isSubstring(sub_count):
#             t_count_copy = t_count.copy()
#             # print(t_count_copy,substring)
#             for char_sub in sub_count.keys():
#                 if char_sub in t_count_copy:
#                     t_count_copy[char_sub] -= sub_count[char_sub]

#             for value in t_count_copy.values():
#                 if value > 0:
#                     return False
#             return True
#         left = 0
#         ans = s
#         tag = False
#         s_count = {}
#         for right in  range(len(s)):
#             s_count[s[right]] = s_count.get(s[right],0) + 1
#             while right - left +1  >=  len(t) and isSubstring(s_count):
#                 tag = True
#                 if len(ans) > right - left + 1:
#                     ans = s[left:right + 1]
#                 s_count[s[left]] -= 1
#                 if s_count[s[left]] == 0:
#                     del s_count[s[left]] 
#                 left += 1
#         if tag: 
#             return ans
        
#         return ''

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""

        map = [0] * 128
        count = len(t)
        start = 0
        end = 0
        min_len = float('inf')
        start_index = 0
        # UPVOTE !
        for char in t:
            map[ord(char)] += 1

        while end < len(s):
            if map[ord(s[end])] > 0:
                count -= 1
            map[ord(s[end])] -= 1
            end += 1

            while count == 0:
                if end - start < min_len:
                    start_index = start
                    min_len = end - start

                if map[ord(s[start])] == 0:
                    count += 1
                map[ord(s[start])] += 1
                start += 1

        return "" if min_len == float('inf') else s[start_index:start_index + min_len]
