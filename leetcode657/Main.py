class Solution:
    def judgeCircle(self, moves):
        mapping = {"U": 0, "D": 0, "L": 0, "R": 0}
        for move in list(moves):
            mapping[move] += 1
        if mapping["U"] != mapping["D"] or mapping["L"] != mapping["R"]:
            return False
        return True


if __name__ == '__main__':
    s = Solution()
    moves = "LL"
    result = s.judgeCircle(moves)
    print(result)