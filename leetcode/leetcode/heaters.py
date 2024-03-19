# class Solution:
#     def findRadius(self, houses: List[int], heaters: List[int]) -> int:
#         heaters.sort()
#         houses.sort()
#         begin = min(houses)
#         last = max(houses)
#         def is_warm_all(radius):
            
#             left, right = 0, 1
#             if len(heaters) > 1:
#                 while right < len(heaters):
                    
                    
#                     if (last - heaters[left] <= radius  and  heaters[left] - radius  <= begin) or (last - heaters[right] <= radius  and  heaters[right] - radius  <= begin):
#                         return True
#                     elif heaters[left] + (2 * radius) + 1 < heaters[right]:
#                         return False
#                     left , right = right, right+1
#             if heaters[0] - radius <= begin and heaters[-1] + radius >= last:
#                 return True
#             else:
#                 return False
#         low, high = 0, pow(10,9)
#         while low < high:
#             mid =  ((low + high) //2)
            
#             if is_warm_all(mid):
#                 print('first')
#                 high = mid
#             else:
#                 low = mid + 1
#             print(mid,low,high)
#         return low

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        if len(heaters) == 1:
            return max(abs(houses[0] - heaters[0]), abs(houses[-1] - heaters[0]))

        m_value = -1
        f, s, ind_heat = heaters[0], heaters[1], 2
        for i in range(len(houses)):
            while houses[i] > s and ind_heat < len(heaters):
                f, s = s, heaters[ind_heat]
                ind_heat += 1
            m_value = max(m_value, min(abs(houses[i] - f), abs(houses[i] - s)))
        return m_value
                


        
            