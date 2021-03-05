class Solution:
    def uniqueOccurrences(self, arr):
        mapping = dict()
        for value in arr:
            if value not in mapping:
                mapping[value] = 1
            else:
                mapping[value] += 1
        return len(list(mapping.values())) == len(set(mapping.values()))


if __name__ == '__main__':
    s = Solution()
    arr = [-3,0,1,-3,1,1,1,-3,10,0]
    result = s.uniqueOccurrences(arr)
    print(result)