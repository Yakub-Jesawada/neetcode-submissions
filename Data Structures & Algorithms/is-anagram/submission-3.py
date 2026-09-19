class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = {}
        for i in s:
            if i in counter.keys():
                counter[i]+=1
            else:
                counter[i]=1
        for j in t:
            if j in counter.keys():
                counter[j]-=1
            else:
                counter[j]=1
        
        result = all(v==0 for v in counter.values())
        return result
