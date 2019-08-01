'''
Input: 100
Output: "202"

Input: -7
Output: "-10"
'''
class Solution:
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num < 0 :
            num=-num
            sym="-"
        else:
            sym=""
        value=[]
        if num >= 0:
            yu=num%7
            value.append(str(yu))
            num=num/7
        value[::-1]
        return sym.join(value)


