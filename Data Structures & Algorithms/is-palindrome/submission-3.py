class Solution:
    def isPalindrome(self, s: str) -> bool:
        char = ""
        for c in s:
            if c.isalpha() == True or c.isdigit():
                char += "".join(c.lower())
            
        reversedstring=''.join(reversed(char))  

        return reversedstring == char
