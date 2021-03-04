class Solution:
    def freqAlphabets(self, s):
        res, i = "", len(s) - 1
        while i > 0:
            if s[i] == '#':
                res += chr(96 + int(s[i-2:i]))
                i -= 3
            else:
                res += chr(96 + int(s[i]))
                i -= 1
        return res[::-1]


if __name__ == '__main__':
    s = Solution()
    string = "10#11#12"
    result = s.freqAlphabets(string)
    print(result)