class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_len = len(s1)
        left=0
        right=len(s1)-1
        window_counter = {}
        s1_counter = {}
        for s in s1:
            s1_counter[s] = s1_counter.get(s,0) + 1
        while right < len(s2):
            for n in s2[left:right+1]:
                window_counter[n] = window_counter.get(n,0)+1
            if s1_counter == window_counter:
                return True
            window_counter={}
            left+=1
            right+=1
        return False
