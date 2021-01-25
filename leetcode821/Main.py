class Solution:
    def shortestToChar(self, S, C):
        path = list()
        for i in range(len(S)):  # 记录有关C字符的索引
            if S[i] == C:
                path.append(i)
        nums = list()
        for value in range(len(S)):
            n = [abs(value-i) for i in path]
            nums.append(min(n))
        return nums


if __name__ == '__main__':
    S = "loveleetcode"
    C = 'e'
    s = Solution()
    print(s.shortestToChar(S,C))