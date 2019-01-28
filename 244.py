class Solution(object):
    def WordDistance(self, words, word1, word2):
        wordDict={}
        for index in range(len(words)):
            if wordDict.has_key(words[index]):
                wordDict[words[index]].append(index)
            else:
                wordDict[words[index]]=[index]

        minLen=len(words)
        for index1 in wordDict[word1]:
            for index2 in wordDict[word2]:
                minLen=min(minLen,abs(index1-index2))
        return minLen



sol=Solution()
print sol.WordDistance (["practice", "makes", "perfect", "coding", "makes"],"coding","practice")