# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

'''
def createList(listArry):
    head=ListNode(listArry[0])
    next=head
    i=1
    while i < len(listArry):
        print listArry[i]
        next.next=ListNode(listArry[i])
        printList(head)
        i=i+1

def printList(head):
    while head!=None:
        print head.val, "->",
    print "\n"
'''
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        retVal=None
        carry=0
        while l1  and l2 and carry:
            sumValue=l1.val+l1.val+carry
            if sumValue>9:
                sumValue=sumValue-10
                carry=1
            newNode=ListNode(sumValue)
            retVal=newNode




'''
sol=Solution()
print sol.addTwoNumbers([2, 7, 11, 15],18)
print sol.addTwoNumbers([3, 2, 4],6)


aa=createList([1,2,3])
printList(aa)
'''