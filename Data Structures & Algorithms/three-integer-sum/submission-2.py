class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        result = []
        for i in range(len(nums)):
            if i > 0 and sorted_nums[i] == sorted_nums[i-1]:
                continue
            target = -sorted_nums[i]
            left = i+1
            right = len(nums) -1
            while left < right:
                sum_val = sorted_nums[left] + sorted_nums[right]
                if left < right and sum_val == target:
                    result.append([sorted_nums[i], sorted_nums[left], sorted_nums[right]])
                    left+=1
                    right-=1
                    while left < right and sorted_nums[left] == sorted_nums[left - 1]:
                        left += 1
                    continue   # <-- go back and recompute sum_val fresh
                if  left < right and sum_val < target:
                    left += 1
                    continue
                if left < right and sum_val > target:
                    right -=1
                    continue
                break
        return result
