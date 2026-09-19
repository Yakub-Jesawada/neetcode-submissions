class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for i in nums:
            if i in counter:
                counter[i] +=1
            else:
                counter[i] = 1
        return sorted(counter, key=lambda x: counter[x], reverse=True)[:k]