class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        rList = list()
        for i in xrange(1,n+1):
            if i%15 == 0:
                rList.append("FizzBuzz")
            elif i%3 == 0:
                rList.append("Fizz")
            elif i%5 == 0:
                rList.append("Buzz")
            else:
                rList.append(str(i))
        return rList