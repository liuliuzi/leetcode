class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return  word.isupper() or word.istitle() or word.islower()
