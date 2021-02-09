class Solution:
    def numJewelsInStones(self, jewels, stones):
        # 哈希表
        mapping = dict()
        for j in jewels:
            mapping[j] = 0
        for stone in stones:
            if stone in mapping:
                mapping[stone] += 1
        k = 0
        for value in mapping.values():
            k += value
        return k


if __name__ == '__main__':
    s = Solution()
    J, S = "aA", "aAAbbbb"
    s.numJewelsInStones(J, S)