class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        滑动窗口
            用两个指针表示字符串中两个子串的左右边界，左指针是子串的开始地址，右指针满足子串不出现重复的字母
            每一次移动左边指针之后，就开始移动右边的指针，但确保没有重复的字母
        """
        occ = set()
        n = len(s)
        ans, right = 0, -1  # 右指针为-1表示没有移动
        for i in range(n):
            if i != 0:
                # 左指针向右移动一格，移除一个字符
                occ.remove(s[i-1])
            while right + 1 < n and s[right + 1] not in occ:
                occ.add(s[right + 1])
                right += 1

            ans = max(ans, right - i + 1)
        return ans


if __name__ == '__main__':
    s = Solution()
    string = "abcabcbb"
    result = s.lengthOfLongestSubstring(string)
    print(result)