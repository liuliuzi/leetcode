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
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
'''
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        def revert(head,end):
            prev = None
            curr = head
            nex = curr.next
        
            #looping
            while curr==end:
                #reversing the link
                curr.next(prev)     

                #moving to next node      
                prev = curr
                curr = nex
                if nex:
                    nex = nex.next

            #initializing head
            head = prev


        i=1
        index=head
        revertStart=head
        while index:
            if i%k==0:
                print "revert start:",revertStart.val,"end:",index.val
                nextstart=index.next
                revert(revertStart,index)
                if i/k==1:
                    head=revertStart
                else:
                    
                index.next=nextstart
                revertStart=index.next
            index=index.next
            i=i+1


sol=Solution()
testList=ListNode(2,ListNode(3,ListNode(4,ListNode(5,ListNode(6,None)))))
print testList
sol.reverseKGroup(testList,2)
#print testList
        