class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for i in nums:
            if i in seen.keys():
                seen[i] +=1
            else:
                seen[i] = 1 
        results = any(v>1 for v in seen.values())
        return results