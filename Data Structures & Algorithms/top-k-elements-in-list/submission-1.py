class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for i in nums:
            counter[i] = counter.get(i,0) + 1
        sorted_items = sorted(counter.items(), key=lambda x: x[1], reverse=True)
        return [key for key, freq in sorted_items[:k]]