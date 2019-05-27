# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
'''
class ListNode(object):
    def __init__(self, x, y):
        self.val = x
        self.next = y
    def __str__(self):
    	j = self
        retStr=""
    	while j:
            retStr += str(j.val)
            if j.next:
                retStr += "->"
            j=j.next
        retStr+=("\n")
        return retStr

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next: return head
        len = 1
        root = head
        while head.next:
            head=head.next
            len=len+1
        n=len-k%len
        head.next=root
        while n >0:
            head=head.next
            n=n-1
        last=head
        head=head.next
        last.next=None

        return head




sol=Solution()
testList=ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,None)))))
print testList
#print sol.rotateRight(testList,2)
print sol.rotateRight(testList,11)
#print testList