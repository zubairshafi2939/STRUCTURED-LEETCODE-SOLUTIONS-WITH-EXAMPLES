class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# List 1: [1, 4, 5]
head1 = ListNode(1)
temp = head1
temp.next = ListNode(4)
temp = temp.next
temp.next = ListNode(5)
temp = temp.next
temp.next = ListNode(9)

head = head1
n = 0
while head:
    n+= 1
    head = head.next
print(9%n)

# for x in range(3):
#     thead = head
#     while thead.next:
#         print(thead.val)
#         last = thead
#         thead  = thead.next
#     thead.next = head
#     head = thead
#     last.next = None



