# class Solution:
#     def characterReplacement(self, s: str, k: int) -> int:
#         left = 0
#         ls = deque([])
#         result = float('-inf')
#         count = 0
#         for right in range(len(s)):
#             if s[right] != s[left] :
#                 ls.append(s[right])
#                 count += 1
#             maxf = max(maxf, count[s[index]])
            
#             while left < right and count > k:
#                 poped = ls.popleft()
#                 if s[left] != poped:  
#                     ls.appendleft(poped)
#                 else:
#                     count -= 1
#                 left += 1
#             result = max(maxf,right-left + 1)
            
#         return result

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        left_pointer = 0
        maxf = 0
        for index in range(len(s)):
            count[s[index]] = 1 + count.get(s[index], 0)
            maxf = max(maxf, count[s[index]])

            if (index - left_pointer + 1) - maxf > k:
                count[s[left_pointer]] -= 1
                left_pointer += 1
            res  = max(maxf, index - left_pointer + 1)
        return res