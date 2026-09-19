class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        prefix = 1
        suffix = 1
        prod_list = [1] * length
        for i,n in enumerate(nums):
            prod_list[i] *= prefix
            prefix*=n
        for j in reversed(range(length)):
            n = nums[j] 
            prod_list[j] *= suffix
            suffix*=n
        return prod_list