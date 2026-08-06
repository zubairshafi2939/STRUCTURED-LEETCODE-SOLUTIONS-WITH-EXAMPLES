# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        def reverseList(head):
            temp = head
            prev = None
            while temp:
                tempo = temp.next #2-3-4
                temp.next = prev #1-none
                prev = temp # 1-none
                temp = tempo
            return prev
        l1 = reverseList(l1)
        l2 = reverseList(l2)
        remainder = 0
        head1 = l1
        head2 = l2
        while l1 and l2:
            num = l1.val + l2.val + remainder
            remainder = num//10
            l1.val = num%10
            l1 = l1.next
            l2 = l2.next
        if l1:
            while l1:
                num = l1.val + remainder
                remainder = num//10
                l1.val = num%10
                l1 = l1.next
        if l2:
            while l2:
                num = l2.val + remainder
                remainder = remainder//10
                l2.val = num%10
                l2 = l2.next
        if remainder:
            l1.next = listNode(remainder)
        return reverseList(head)
            
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        

