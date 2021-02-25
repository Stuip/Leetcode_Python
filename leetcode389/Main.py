class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s, t = list(s), list(t)
        for c in s:
            t.remove(c)
        return "".join(t)


if __name__ == '__main__':
    res = Solution()
    s, t = "a", "aa"
    result = res.findTheDifference(s,t)
    print(result)