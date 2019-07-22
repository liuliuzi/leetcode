class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        t1 = 0
        for i in num1:
            t1 *= 10
            t1 += ord(i) - 48


        t2 = 0
        for i in num2:
            t2 *= 10
            t2 += ord(i) - 48

        return str(t1 + t2)