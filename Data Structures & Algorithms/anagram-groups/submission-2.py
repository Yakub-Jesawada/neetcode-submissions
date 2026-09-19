class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapper = {}
        for i in strs:
            sorted_string = "".join(sorted(i))
            mapper.setdefault(sorted_string, []).append(i)
            # group = mapper.get(sorted_string,[])
            # group.append(i)
            # mapper[sorted_string] = group
        return list(mapper.values())