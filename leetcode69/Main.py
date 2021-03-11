class Solution:
    def mySqrt(self, x: int) -> int:
        """
        不用Python的内置函数
        算法思想--- 二分查找法：
            由于x的平方根的整数部分ans是满足K ** 2 <= x的最大值
        算法思想： 牛顿迭代法
        :param x:
        :return:
        """
        # 二分查找法
        left, right, ans = 0, x, -1
        while left <= right:
            mid = (left + right) >> 1
            if mid ** 2 <= x:  # mid的平方值小于x，说明x的平方根在mid右区间
                ans = mid
                left = mid + 1
            else:              # mid的平方根大于x，说明x的平方根在mid左区间
                right = mid - 1
        return ans





if __name__ == '__main__':
    s = Solution()
    result = s.mySqrt(x=4)
    print(result)