class Solution:
    def balancedStringSplit(self, s):
        num, result = 0, 0
        for c in s:
            if c == "R":
                num += 1
            else:
                num -= 1
            if num == 0:
                result += 1
        return result


if __name__ == '__main__':
    s = Solution()
    string = "RLRRLLRLRL"
    result = s.balancedStringSplit(string)
    print(result)