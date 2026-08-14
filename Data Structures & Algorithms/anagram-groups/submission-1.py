class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Idea is to count each letter and compare so - 
        #eat = 1e,1a,1t - tea = 1e,1a,1t
        res = defaultdict(list) #Map charCount to list of anagrams

        for s in strs:
            count = [0] * 26 # a..z

            for c in s:
                count[ord(c) - ord("a")] += 1
        
            res[tuple(count)].append(s)
       
        return list(res.values())