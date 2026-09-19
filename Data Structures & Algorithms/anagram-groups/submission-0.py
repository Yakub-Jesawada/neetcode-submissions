class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapper = {}
        for i in strs:
            sorted_i = "".join(sorted(i))  # e.g. "eat" → "aet"

            if sorted_i in mapper:
                mapper[sorted_i].append(i)
            else:
                mapper[sorted_i] = [i]
        output = []
        for i in mapper:
            output.append(mapper[i])
        return output