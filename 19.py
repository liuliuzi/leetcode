# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, y):
        self.val = x
        self.next = y
    def printList(self):
    	j = self
    	while j:
        	print j.val, "->",
        	j=j.next
        print "\n"

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: L
        """
        j = head
        while n > 1 :
            j=j.next
            n = n-1
        if j.next==None:
        	return  head.next
        pre = head
        i=head.next
        j=j.next
        while j.next!= None:
        	pre = pre.next
        	i=i.next
        	j=j.next
        if i!=None:
            pre.next = i.next
        else:
        	pre.next = None
        return head









sol=Solution()
testList=ListNode(2,ListNode(3,ListNode(4,ListNode(5,ListNode(6,None)))))
testList.printList()
sol.removeNthFromEnd(testList,5).printList()
testList.printList()
sol.removeNthFromEnd(testList,2).printList()
