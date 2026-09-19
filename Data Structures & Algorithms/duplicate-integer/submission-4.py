class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for i in nums:
            seen[i] = seen.get(i,0) + 1
        result = any(v>1 for v in seen.values())
        return result
