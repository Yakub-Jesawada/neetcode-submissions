class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapper = {}
        for string in strs:
            sorted_str = "".join(sorted(string))
            group = mapper.get(sorted_str,[])
            group.append(string)
            mapper[sorted_str] = group
        return list(mapper.values())