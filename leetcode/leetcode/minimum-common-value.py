class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        nums1 =list(set(nums2)) +list(set(nums1))
        nums1.sort()
        for i in range(1,len(nums1)):
            if nums1[i-1] == nums1[i]:
                return nums1[i]
        return -1
