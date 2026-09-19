class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,n in enumerate(nums):
            remainder = target - n
            if remainder in nums[i+1:]:
                j = nums[i+1:].index(remainder) + i + 1
                return [i,j]

