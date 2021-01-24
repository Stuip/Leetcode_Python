class Solution:

    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        ans = list()
        text = text.split(" ")
        index = 0
        while index < len(text):
            part = text[index:index+3]
            if len(part) < 3:
                break
            if part[0] == first and part[1] == second:
                ans.append(part[2])
            index += 1
        return ans