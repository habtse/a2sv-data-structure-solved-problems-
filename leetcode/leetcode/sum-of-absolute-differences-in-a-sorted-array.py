class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        res = []

        prefix_sum = 0
        suffix_sum = sum(nums)

        for i, num in enumerate(nums):
            left_sum = num * i - prefix_sum

            right_sum = suffix_sum - num * (len(nums) - i)

            total_sum = left_sum + right_sum

            res.append(total_sum)

            prefix_sum += num
            suffix_sum -= num

        return res        