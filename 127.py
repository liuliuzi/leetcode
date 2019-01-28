class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        q = [(beginWord,1)]
        while q:
            e,lens = q.pop(0)
            if e == endWord: return lens
            for i in range(len(e)):
                left = e[:i]
                right = e[i + 1:]
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    if e[i] != c:
                        nextWord = left + c + right
                        if nextWord in wordList:
                            q.append((nextWord,lens + 1))
                            wordList.remove(nextWord)
        return 0

sol=Solution()
print sol.ladderLength("hit","cog",["hot","dot","dog","lot","log","cog"])