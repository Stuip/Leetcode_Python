class Solution:
    def shuffle(self, nums, n):
        new_nums = list()
        for index in range(n):
            new_nums.append(nums[index])
            new_nums.append(nums[index+n])
        return new_nums