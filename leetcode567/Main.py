class Solution:
    def checkInclusion(self, s1, s2) -> bool:
        mapping = dict()
        for value in s1:
            if value not in mapping:
                mapping[value] = 1
            else:
                mapping[value] += 1


if __name__ == '__main__':
    s = Solution()
    s1 = "ab"
    s2 = "eidbaooo"
