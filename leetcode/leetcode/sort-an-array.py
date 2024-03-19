class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left_half,right_half) -> List[int]:
            # write your code here
            pt1 , pt2 = 0,0
            sorted_array = []
            
            while pt1 < len(left_half) and pt2 < len(right_half):
                if left_half[pt1] < right_half[pt2]:
                    
                    sorted_array.append(left_half[pt1])
                    pt1 +=1
                else:
                    
                    sorted_array.append(right_half[pt2])
                    pt2 +=1
            if pt1 < len(left_half):
                sorted_array.extend(left_half[pt1:])
            else:
                sorted_array.extend(right_half[pt2:])
            return sorted_array
                    
            
                    

        def mergeSort(left, right, arr):
            if left == right:
                return [arr[left]]
            mid = left + (right - left) // 2
            left_half = mergeSort(left, mid, arr)
            right_half = mergeSort(mid + 1, right, arr)
        
            return merge(left_half, right_half)
        return mergeSort(0,len(nums)-1,nums)