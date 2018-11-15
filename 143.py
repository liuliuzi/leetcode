
class ListNode(object):
    def __init__(self, x, next):
        self.val = x
        self.next = next

    def __str__(self):
    	cur = self  
    	retStr = ""      
        while cur != None:
        	retStr =retStr + str(cur.val)
        	if cur.next!=None:
        		retStr = retStr + "->"
        	cur=cur.next
        return retStr


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        #reverse
        if head == None or head.next == None:
            return

        pre = head
        lat = head.next
        while lat != None and lat.next != None:
            pre = pre.next
            lat = lat.next.next
        p = pre.next
        pre.next = None


        cur = None        
        while p != None:
            q = p.next
            p.next = cur
            cur = p 
            p = q


        pre = head
        while pre != None and cur != None:
            tmp = cur.next  
            cur.next = pre.next
            pre.next = cur
            pre = pre.next.next
            cur = tmp 

sol=Solution()

ln=ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,ListNode(6,None))))))
print ln
print sol.reorderList(ln)

