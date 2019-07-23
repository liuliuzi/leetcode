class Solution(object):
    def findWords(self, words):
        keyboard = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]

        out = []

        for i in words:
            for line in keyboard:
                lword = i.lower()
                if set(lword).issubset(set(line)):
                    out.append(i)

        return out
