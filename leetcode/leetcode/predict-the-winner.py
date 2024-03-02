
class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def score_diff(lo, hi):
            if lo == hi:
                return nums[lo]

            return max(nums[lo]-score_diff(lo+1, hi), nums[hi]-score_diff(lo, hi-1))

        return score_diff(0, len(nums)-1) >= 0


# class Solution:
#     def predictTheWinner(self, nums: List[int]) -> bool:
#         result1 = 0
#         result2 = 0
#         def predict(left,right, turn):
#             nonlocal result1, result2
#             if left == right:
#                 if turn:
#                     return [nums[right],0]
#                 return [0,nums[right]]
#             if turn:
#                 choice1 = predict(left + 1, right,not turn)
#                 choice2 = predict(left,right -1 , not turn)
#                 result1 = max(choice1[0],choice2[0])
                
#                 return ([min(choice1[0],choice2[0]),max(nums[left],nums[right])])
#             else:
#                 choice1 = predict(left + 1, right,not turn)
#                 choice2 = predict(left,right -1 , not turn)
#                 result2 += max(choice1[1],choice2[1])
#                 return ([max(nums[left],nums[right]),min(choice1[1],choice2[1])])
        
#         predict(0,len(nums)-1, True)
#         if result1 < result2:
#             return False
#         return True
            


            
