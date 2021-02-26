class Solution:
    def titleToNumber(self, s):
        num = 0
        string = list(s.lower())[::-1]
        for i in range(len(string)):
            n = ord(string[i]) - ord("a") + 1
            num += n * pow(26, i)
        return num


if __name__ == '__main__':
    s = Solution()
    string = "A"
    s.titleToNumber(string)