class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        for i in range(len(s)):
            s[i] = s[i][::-1]
        return " ".join(s).rstrip()


if __name__ == '__main__':
    s = Solution()
    string = "Let's take LeetCode contest"
    result = s.reverseWords(string)
    print(result)
