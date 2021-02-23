class Solution:
    def check(self, nums):
        sorted_nums = sorted(nums)
        index = 0
        while index < len(nums) - 1:
            if nums[index + 1] < nums[index]:
                break
            index += 1
        if index == len(nums) - 2:  # 说明是排序好的列表
            return True
        nums = nums[index + 1:] + nums[:index + 1]
        for i in range(len(nums)):
            if sorted_nums[i] != nums[i]:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    nums = [1,2,3]
    result = s.check(nums)
    print(result)