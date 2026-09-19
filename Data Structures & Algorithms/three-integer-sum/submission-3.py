class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        sorted_nums = sorted(nums)
        for i in range(len(nums)):
            if i > 0 and sorted_nums[i] == sorted_nums[i-1]:
                continue
            left = i+1
            right = len(nums) - 1
            target = -sorted_nums[i]
            while left < right:
                sum_val = sorted_nums[left] + sorted_nums[right]
                if left < right and sum_val == target:
                    result.append([sorted_nums[i], sorted_nums[left], sorted_nums[right]])
                    right-=1
                    left+=1
                    while left < right and sorted_nums[left] == sorted_nums[left-1]:
                        left+=1
                    continue
                if left < right and sum_val > target:
                    right -=1
                    continue
                if left < right and sum_val < target:
                    left+=1
                    continue
        return result
