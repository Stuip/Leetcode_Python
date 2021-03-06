class Solution:
    def countMatches(self, items, ruleKey, ruleValue):
        res = 0
        for item in items:
            mapping = dict()
            mapping["type"], mapping["color"], mapping["name"] = item
            if mapping[ruleKey] ==  ruleValue:
                res += 1
        return res


if __name__ == '__main__':
    s = Solution()
    items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]]
    ruleKey = "type"
    ruleValue = "phone"
    result = s.countMatches(items, ruleKey, ruleValue)
    print(result)