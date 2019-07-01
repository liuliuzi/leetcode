# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
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
'''
Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
'''
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        elList=ListNode(0,None)
        ltList=ListNode(0,None)
        elHead,ltHead=elList,ltList
        while head:
            if head.val < x:
                elList.next = head
                elList = elList.next
            else:
                ltList.next = head
                ltList = ltList.next
            temp = head.next
            head.next = None
            head = temp
        elList.next  = ltHead.next

        return elHead.next


sol=Solution()
testList=ListNode(1,ListNode(4,ListNode(3,ListNode(2,ListNode(5,ListNode(2,None))))))
print testList
print sol.partition(testList,3)