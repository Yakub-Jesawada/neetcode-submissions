class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_len = len(s1)
        left=0
        right=len(s1)-1
        window_counter = {}
        s1_counter = {}
        for s in s1:
            s1_counter[s] = s1_counter.get(s,0) + 1
        for s in s2[left:right+1]:
            window_counter[s] = window_counter.get(s,0) + 1
        while right < len(s2):
            if s1_counter == window_counter:
                return True
            window_counter[s2[left]] -= 1
            if window_counter[s2[left]] == 0:
                del window_counter[s2[left]]
            left+=1
            right+=1
            if right < len(s2):
                window_counter[s2[right]] = window_counter.get(s2[right],0) + 1
        return False
