class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        lo = 0
        hi = len(people)-1
        boats = 0
        while lo <= hi:
            if people[lo] + people[hi] <= limit:
                lo += 1
                hi -= 1
            else:
                hi -= 1
            boats += 1
        return boats
#  class Solution:
#     def numRescueBoats(self, people: List[int], limit: int) -> int:
#         people.sort()
#         left,right = 0,len(people)-1
#         count =0
#         total =people[left] + people[right]
#         for i in range(len(people)):
#             if right ==left+1:
#                 if total> limit:
#                     count +=2
#                 else:
#                     count +=1
#                 break

#             elif total >=limit :
#                 if total ==limit:
#                     left +=1
#                     total -=people[left]
#                 count +=1
#                 total -=people[right]
#                 right -=1
#                 total+=people[right]
                
            
#             else:
                
#                 left += 1
#                 total +=people[left]
#         return count
