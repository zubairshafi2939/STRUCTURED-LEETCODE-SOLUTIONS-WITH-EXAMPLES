# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        if not head or head.next == None:
            return head
        check = head
        n = 0
        while check:
            n+=1
            check = check.next
        k = k%n
        for x in range(k):
            thead = head
            while thead.next:
                print(thead.val)
                last = thead
                thead  = thead.next
            thead.next = head
            head = thead
            last.next = None
        return head

        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        