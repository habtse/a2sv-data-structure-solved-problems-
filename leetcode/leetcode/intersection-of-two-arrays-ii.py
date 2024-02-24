class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output=[]
        if len(nums1)<len(nums2):
            for i in nums1:
                if i in nums2:
                    output.append(i)
                    nums2[nums2.index(i)] =-1
        else:
            for i in nums2:
                if i in nums1:
                    output.append(i)
                    nums1[nums1.index(i)] =-1
        return output
            

