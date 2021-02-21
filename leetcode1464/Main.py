class Solution:
    def maxProduct(self, nums):
        nums.sort()
        return (nums[-1] - 1) * (nums[-2] - 1)



if __name__ == '__main__':
    s = Solution()
    nums = [1,5,4,5]
    result = s.maxProduct(nums)
    print(result)