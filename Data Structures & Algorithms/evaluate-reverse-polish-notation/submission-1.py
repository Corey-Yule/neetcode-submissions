class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num = []
        symbols = ["+", "-", "*", "/"]

        for char in tokens:
            if char in symbols:
                a = num.pop()
                b = num.pop()

                if char == "+":
                    num.append(b + a)
                elif char == "-":
                    num.append(b - a)
                elif char == "*":
                    num.append(b * a)
                elif char == "/":
                    num.append(int(b / a))
            else:
                num.append(int(char))

        return num[0]