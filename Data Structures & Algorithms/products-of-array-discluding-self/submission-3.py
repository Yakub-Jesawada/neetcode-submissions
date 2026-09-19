class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        prefix_list = [1] * length
        suffix_list = [1] * length
        prod_list = [1] * length
        prefix = 1
        suffix = 1
        for i,n in enumerate(nums):
            prefix_list[i] = prefix
            prefix *= n
        for j in reversed(range(length)):
            n = nums[j]
            suffix_list[j] = suffix
            suffix *=n
        for x in range(length):
            prod_list[x] = prefix_list[x] * suffix_list[x]
        return prod_list