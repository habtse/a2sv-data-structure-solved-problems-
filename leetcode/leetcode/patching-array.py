class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        count =0         # count the number of patchs
        total = 1        # total sum of the elements
        index =0
        while total<=n:
            
            
            if index == len(nums) :
                print(total)
                total +=total +1
                count +=1
            elif total >= nums[index]  :
                
                total += nums[index]
                index +=1
            
                
            else :
                print(total)
                count +=1              # patch one element                 
                total +=total          # total become the total sum of the elements with patch plus one
            
        return count




                