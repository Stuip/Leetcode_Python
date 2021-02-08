class Solution:
    def largestAltitude(self, gain):
        num,max_height = 0, 0
        for value in gain:
            num += value
            if num > max_height:
                max_height = num
        return max_height