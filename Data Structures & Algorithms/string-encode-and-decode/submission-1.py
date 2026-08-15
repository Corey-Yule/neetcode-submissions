class Solution:
    def encode(self, strs: List[str]) -> str:
        a = ""
        for s in strs:
           a += str(len(s))
           a += "".join("#")
           a += "".join(s)
        # print(a)
        return a


    def decode(self, s: str) -> List[str]:
        res, i =[],0

        if len(s) <=0:
            return []
        
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])

            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length

        return res