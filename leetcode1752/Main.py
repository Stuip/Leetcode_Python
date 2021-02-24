class Solution:
    def check(self, nums):
        flag = nums[0] >= nums[len(nums) - 1]  # 是否有轮转
        for index in range(1,len(nums)):
            if nums[index] < nums[index-1]:
                if flag:
                    flag = False
                else:
                    return False
        return True


if __name__ == '__main__':
    s = Solution()
    nums = [1,2,3]
    result = s.check(nums)
    print(result)