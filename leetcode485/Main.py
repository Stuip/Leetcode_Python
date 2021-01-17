class Solution:
    """
    解法一思路：
        首先将列表中的数字转换为字符串
    """
    """
    解法一
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        nums = [str(value) for value in nums]    # nums = list(map(str, nums))
        nums = "".join(nums)
        nums = nums.split("0")
        k = 0 
        for value in nums:
            length = len(value)
            if length > k:
                k = length
        return k
    """
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # 解法二
        count = 0
        result = 0
        for value in nums:
            if value == 1:
                count += 1
            else:
                result = max(result, count)
                count = 0
        return max(result,count)