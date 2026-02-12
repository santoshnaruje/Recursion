from curses.ascii import isdigit

class Solution:
    INT_MIN = -2**31
    INT_MAX = 2**31 - 1

    def helper(self, s, i, num, sign):

        if i == len(s) or not isdigit(s[i]):
            return num * sign

        num = num * 10 + int(s[i])

        if sign * num <= self.INT_MIN:
            return self.INT_MIN

        if sign * num >= self.INT_MAX:
            return self.INT_MAX

        return self.helper(s, i + 1, num, sign)

    def myAtoi(self, s: str) -> int:
        i = 0
        sign = 1

        while i < len(s) and s[i] == ' ':
            i += 1

        if i < len(s) and (s[i] == '+' or s[i] == '-'):
            sign = 1 if s[i] == '+' else -1
            i += 1

        return self.helper(s, i, 0, sign)

if __name__ == '__main__':
    # s = " -042"
    s = "-91283472332"
    sol = Solution()
    res = sol.myAtoi(s)
    print(res)
