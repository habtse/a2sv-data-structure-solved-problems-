class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ls =[]
        for i in nums1:
            nextIndex2 = nums2.index(i) +1
            tag = False
            for i in range(nextIndex2,len(nums2)):
                
                if nums2[i] > nums2[nextIndex2 -1]:
                    ls.append(nums2[i])
                    tag = True
                    break
                
            if not tag :
                ls.append( -1)
        return ls