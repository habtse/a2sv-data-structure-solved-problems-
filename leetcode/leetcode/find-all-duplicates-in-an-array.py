class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        s = Counter(nums)
        return [num for num,freq in s.items() if freq == 2]