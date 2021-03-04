class Solution:
    def maxEnvelopes(self, envelopes):
        for length, width  in envelopes:
            print(length, width)


if __name__ == '__main__':
    s = Solution()
    envelopes = [[5,4],[6,4],[6,7],[2,3]]
    s.maxEnvelopes(envelopes)


