# Time complexity - O(n)
# Space complexity - O(1)

# Approach - Maintain 4 variables and update then based on the formulae (straightforward, this leetcode
# problem is more about memorizing the pattern) update the values. Note: the number needs to be dealt with
# first, otherwise gets error.

class Solution:
    def calculate(self, s: str) -> int:
        if s == None or len(s) == 0:
            return 0
        
        num = 0
        calc = 0
        tail = 0
        lastSign = "+"

        for i in range(len(s)):
            if s[i].isdigit():
                num = num*10 + (int)(s[i])
            # if (i == len(s) - 1) or (s[i] in ["+", "-", "*", "/"] and s[i] != " "):
            if (i == len(s) - 1) or (not s[i].isdigit() and s[i] != " "):
                if lastSign == "+":
                    calc = calc + num
                    tail = num
                if lastSign == "-":
                    calc = calc - num
                    tail = - num
                if lastSign == "*":
                    calc = calc - tail + tail * num
                    tail = tail * num
                if lastSign == "/":
                    calc = calc - tail + int(tail/num)
                    tail = int(tail/num)
                # if i == len(s) - 1:
                #     num = 0
                # else:
                lastSign = s[i]
                num = 0
                print(num, calc, tail, lastSign)
            # elif s[i] == " ":
            #     continue
        return calc