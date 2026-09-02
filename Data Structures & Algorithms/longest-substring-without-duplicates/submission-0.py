class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check = set()
        l = 0
        counter = 0
        for r in range(len(s)):
            while s[r] in check:
                check.remove(s[l])
                l +=1
            check.add(s[r])
            counter = max(counter, r-l + 1)
        
        return counter
