class Solution:
    """
    通过两个栈来实现   stack来储存大于当前遍历元素值(默认为[-1,])
            不断将nums2栈不断弹出，直到等于当前元素nums1[i]
                如果大于nums1[i]就压入栈中
    最后弹出stack栈顶元素
    """
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        for i in range(len(nums1)):
            stack = [-1,]
            index = nums2.index(nums1[i])
            while index < len(nums2):
                if nums2[index] > nums1[i]:
                    stack.append(nums2[index])
                    break
                index += 1
            nums1[i] = stack.pop()
        return nums1