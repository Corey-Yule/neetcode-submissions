class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for v in strs:
            curr = "".join(sorted(v))
            res[curr].append(v)
        
        return list(sorted(res.values()))