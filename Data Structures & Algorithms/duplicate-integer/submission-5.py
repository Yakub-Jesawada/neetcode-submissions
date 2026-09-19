class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = {}
        for n in nums:
            counter[n] = counter.get(n,0) + 1
        return any(v>1 for v in counter.values())