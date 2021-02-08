class Solution:
    def numIdenticalPairs(self, nums):
        k = 0
        for index in range(len(nums)):
            num = nums[index+1:].count(nums[index])
            k += num
        print(k)


if __name__ == '__main__':
    s = Solution()
    nums = [1,2,3,1,1,3]
    s.numIdenticalPairs(nums)