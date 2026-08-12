class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tl = []
        sl = []
        if len(s) != len(t):
            return False

        for char in s:
            sl.append(char)
        for char in t:
            tl.append(char)
        
        sl.sort()
        tl.sort()

        if sl == tl:
            return True
        else: 
            print("Not The Same")
            return False