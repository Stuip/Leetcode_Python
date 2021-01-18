"""
给你一个数组 nums和一个值 val，你需要 原地 移除所有数值等于val的元素，并返回移除后数组的新长度。

不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
"""
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if nums is None or len(nums) == 0:    # 判断nums是否为空或者nums没有元素
            return 0
        i,j=0,len(nums)-1

        while(i<j):
            while i<j and nums[i] != val:
                i += 1
            while i<j and nums[j] == val:
                j -= 1
            nums[i],nums[j] = nums[j],nums[i]
        if nums[i] == val:
            return i;
        else:
            return i+1;