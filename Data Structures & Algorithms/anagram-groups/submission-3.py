class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        groups = {}
        # Loop through the word in the strings
        for word in strs:
            #sort the words
            sort = "".join(sorted(word))
            # if the sorted word is in the groups array then link them together 
            #(put them in  the same list)
            if sort in groups:
                groups[sort].append(word)
            else:
                #first word in the groups list
                groups[sort] = [word]
        
        for i, group in groups.items():
            res.append(group)

        return res