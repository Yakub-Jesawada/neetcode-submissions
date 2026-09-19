class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_split = sorted(s)
        t_split = sorted(t)
        if t_split == s_split:
            return True
        return False