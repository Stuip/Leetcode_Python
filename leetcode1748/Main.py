class Solution:
    def sumOfUnique(self, nums):
        mapping = dict()
        for value in nums:
            if value not in mapping:
                mapping[value] = 1
            else:
                mapping[value] += 1
        sum = 0
        for key, value in mapping.items():
            if value == 1:
                sum += key
        return sum