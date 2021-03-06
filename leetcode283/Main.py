class Solution:
    """
    给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
    """
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        k = 0
        for value in nums:    ## 记录几个0的数
            if value == 0:
                k += 1
        i = 0
        j = 0
        while(i<len(nums)):  # 将不为零的值向前移到前面
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
            i += 1
        while k > 0:
            nums[k*-1] = 0
            k -= 1
        """
        # 双指针
        index = 0   # 指向存放非零元素的索引
        for value in nums:
            if value != 0:
                nums[index] = value
                index += 1
        while index < len(nums):
            nums[index] = 0
            index += 1