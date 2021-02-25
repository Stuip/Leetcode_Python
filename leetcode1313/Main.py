class Solution:
    def decompressRLElist(self, nums):
        res = list()
        n = len(nums)
        for i in range(n):
            if 2 * i < n and 2 * i + 1 < n:
                res += [nums[2*i + 1]] * nums[2 * i]
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [1,2,3,4]
    result = s.decompressRLElist(nums)
    print(result)

