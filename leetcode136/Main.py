class Solution:
    def singleNumber(self, nums):
        mapping = dict()
        for value in nums:
            if value not in mapping:
                mapping[value] = 1
            else:
                mapping[value] += 1
        for key, value in mapping.items():
            if value == 1:
                return key


if __name__ == '__main__':
    s = Solution()
    nums = [2,2,1]
    result = s.singleNumber(nums)
    print(result)