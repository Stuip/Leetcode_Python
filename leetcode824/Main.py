class Solution:
    def toGoatLatin(self, S):
        dig = ("a", "e", "i", "o", "u")
        S = S.split(" ")
        for i in range(len(S)):
            if S[i][0].lower() in dig: # 单词以元音开头
                S[i] = S[i] + "ma" + "a" * (i+1)
            else:
                S[i] = S[i][1:] + S[i][0] + "ma" + "a" * (i+1)
        S = " ".join(S).rstrip()
        return S


if __name__ == '__main__':
    s = Solution()
    S = "I speak Goat Latin"
    s.toGoatLatin(S)