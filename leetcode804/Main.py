class Solution:
    def uniqueMorseRepresentations(self, words):
        pwd = [".-", "-...", "-.-.", "-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        dig = [chr(i+ord("a")) for i in range(26)]
        mapping = dict(zip(dig, pwd))
        res = set()
        for word in words:
            string = ""
            for c in list(word):
                string += mapping[c]
            res.add(string)
        return len(res)



if __name__ == '__main__':
    s = Solution()
    words = ["gin", "zen", "gig", "msg"]
    result = s.uniqueMorseRepresentations(words)
    print(result)