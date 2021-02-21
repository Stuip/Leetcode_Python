class Solution:
    def halvesAreAlike(self, s):
        mappingf = {'a':0, 'e': 0,'i': 0, 'o': 0, 'u': 0}
        mappingb = {'a':0, 'e': 0,'i': 0, 'o': 0, 'u': 0}
        mid = len(list(s)) // 2
        front, back = s[:mid].lower(), s[mid:].lower()
        for f in front:
            if f in mappingf:
                mappingf[f] += 1
        for b in back:
            if b in mappingb:
                mappingb[b] += 1
        return sum(mappingf.values()) == sum(mappingb.values())


if __name__ == '__main__':
    s = Solution()
    s1 = "AbCdEfGh"
    result = s.halvesAreAlike(s1)
    print(result)