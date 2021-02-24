class Solution:
    def destCity(self, paths) -> str:
        mapping = dict()
        for path in paths:
            for value in path:
                if value not in mapping:
                    mapping[value] = 1
                else:
                    mapping[value] += 1
        last = [key for key,value in mapping.items() if value == 1]
        for m,n in paths:
            if m in last:
                last.remove(m)
        return last[0]


if __name__ == '__main__':
    s = Solution()
    paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
    result = s.destCity(paths)
    print(result)