class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = {}
        for i in s:
            counter[i] = counter.get(i,0) + 1
        for j in t:
            counter[j] = counter.get(j,0) - 1
        return all(v==0 for v in counter.values())