class Solution:
    def runningSum(self, nums):
        tmp = nums[:]
        for index in range(1, len(tmp)+1):
            nums[index-1] = sum(tmp[:index])
        print(nums)


if __name__ == '__main__':
    s = Solution()
    nums = [1,2,3,4]
    s.runningSum(nums)