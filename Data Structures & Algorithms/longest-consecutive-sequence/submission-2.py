class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        current = 0
        sorted_nums = sorted(nums)
        for i,n in enumerate(sorted_nums):
            if i == 0:
                current += 1
            if i == len(nums) - 1:
                continue
            if n == sorted_nums[i+1]:
                continue
            if n + 1 ==  sorted_nums[i+1]:
                current += 1
            else:
                current = 1
            longest = max(longest, current)
        return max(longest, current)

        